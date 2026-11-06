#!/usr/bin/env python3
"""Local preview server that mimics GitHub Pages pretty URLs.

Serves the repository root and resolves /techtopics to techtopics.html so links
work exactly as they will on the live site.

Usage: python3 scripts/preview_server.py [port]
"""
import http.server
import os
import socketserver
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def send_head(self):
        path = self.path.split("?")[0].split("#")[0]
        local = self.translate_path(path)
        # Match GitHub Pages: /software resolves software.html even when a
        # same-named directory exists.
        if not path.endswith("/") and "." not in os.path.basename(path):
            html = local + ".html"
            if os.path.exists(html):
                self.path = path + ".html"
        return super().send_head()

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("0.0.0.0", port), Handler) as httpd:
        print(f"preview server on http://0.0.0.0:{port}", flush=True)
        httpd.serve_forever()
