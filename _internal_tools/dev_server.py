import http.server
import socketserver
import os
import sys

# Auto-detect website root (whether run from project root or from _internal_tools)
script_dir = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(script_dir) == '_internal_tools':
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
else:
    project_root = script_dir

os.chdir(project_root)
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        clean_path = self.path.split('?')[0].split('#')[0]
        local_path = clean_path.lstrip('/')
        qs = self.path[len(clean_path):]

        # 1. If path ends in .html (and not index.html), redirect to clean URL with 308
        if clean_path.endswith('.html') and clean_path != '/index.html':
            redirect_target = clean_path[:-5] + qs
            self.send_response(308)
            self.send_header('Location', redirect_target)
            self.end_headers()
            return

        # 2. If root, serve index.html
        if not local_path:
            return super().do_GET()

        # 3. If exact file or directory exists, serve normally
        if os.path.exists(local_path):
            return super().do_GET()

        # 4. If path + .html exists, serve .html file under clean URL
        if os.path.exists(local_path + '.html'):
            self.path = clean_path + '.html' + qs
            return super().do_GET()

        return super().do_GET()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
        print(f"Clean URL dev server running at http://127.0.0.1:{PORT}/")
        print(f"Serving files from: {project_root}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
