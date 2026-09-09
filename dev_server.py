import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Extract path without query or anchor
        clean_path = self.path.split('?')[0].split('#')[0]
        local_path = clean_path.lstrip('/')
        qs = self.path[len(clean_path):]

        # 1. If user enters a path ending in .html (e.g. /guide/foo.html), redirect to clean URL /guide/foo
        if clean_path.endswith('.html') and clean_path != '/index.html':
            redirect_target = clean_path[:-5] + qs
            self.send_response(308) # Permanent redirect
            self.send_header('Location', redirect_target)
            self.end_headers()
            return

        # 2. If root, serve index.html
        if not local_path:
            return super().do_GET()

        # 3. If exact file or directory exists, serve normally
        if os.path.exists(local_path):
            return super().do_GET()

        # 4. If path + .html exists, rewrite internally to serve the .html file under the clean URL
        if os.path.exists(local_path + '.html'):
            self.path = clean_path + '.html' + qs
            return super().do_GET()

        return super().do_GET()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
        print(f"Clean URL dev server running at http://127.0.0.1:{PORT}/")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
