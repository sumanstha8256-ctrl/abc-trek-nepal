import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

REDIRECTS = {
    '/guide/annapurna-base-camp-trek-ultimate-guide': '/guide/annapurna-base-camp-trek',
    '/guide/annapurna-base-camp-trek-ultimate-guide.html': '/guide/annapurna-base-camp-trek',
}

class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        url_path = self.path.split('?')[0].split('#')[0]
        query = ('?' + self.path.split('?')[1]) if '?' in self.path else ''

        # 1. Check custom permanent redirects (matches vercel.json redirects)
        if url_path in REDIRECTS:
            self.send_response(301)
            self.send_header('Location', REDIRECTS[url_path] + query)
            self.end_headers()
            return

        # 2. Redirect any .html requests to extensionless clean URLs (matches Vercel cleanUrls)
        if url_path.endswith('.html'):
            clean = url_path[:-5]
            if clean.endswith('/index'):
                clean = clean[:-6] or '/'
            elif clean == '/index':
                clean = '/'
            # If the clean target has a redirect, follow it
            target = REDIRECTS.get(clean, clean)
            self.send_response(301)
            self.send_header('Location', target + query)
            self.end_headers()
            return

        # 3. Handle directory / clean path lookups
        clean_path = url_path.rstrip('/') if url_path != '/' else '/'
        local_path = self.translate_path(clean_path)

        # Check if clean_path.html exists (e.g. /plan-your-trek -> /plan-your-trek.html)
        if not os.path.exists(local_path) and os.path.exists(local_path + '.html'):
            self.path = clean_path + '.html' + query
        # Check if clean_path is a directory with index.html (e.g. /treks -> /treks/index.html)
        elif os.path.isdir(local_path) and os.path.exists(os.path.join(local_path, 'index.html')):
            if not url_path.endswith('/'):
                self.path = clean_path + '/index.html' + query

        return super().do_GET()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    print(f"Clean URL dev server running on http://127.0.0.1:{PORT}")
    with socketserver.TCPServer(('127.0.0.1', PORT), CleanUrlHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
