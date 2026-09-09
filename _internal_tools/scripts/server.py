import http.server
import socket
import socketserver
import os
import sys

PORT = 3000
DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

class DualStackServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    address_family = socket.AF_INET6

    def server_bind(self):
        # Enable dual-stack (IPv6 + IPv4 on the same port)
        try:
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        except Exception:
            pass
        super().server_bind()

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        sys.stderr.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))
        sys.stderr.flush()

def run():
    try:
        httpd = DualStackServer(("::", PORT), CustomHandler)
        print(f"Dual-stack server running on port {PORT}")
        print(f"URL: http://localhost:{PORT}/")
        print(f"URL: http://127.0.0.1:{PORT}/")
        sys.stdout.flush()
        httpd.serve_forever()
    except Exception as e:
        print(f"Dual-stack failed ({e}), starting standard IPv4 server...")
        httpd = socketserver.TCPServer(("0.0.0.0", PORT), CustomHandler)
        print(f"IPv4 server running on http://localhost:{PORT}/")
        sys.stdout.flush()
        httpd.serve_forever()

if __name__ == "__main__":
    run()
