#!/usr/bin/env python3
# 本地预览/临时使用：在 pwa 目录运行 `python3 serve.py`，手机连同一 WiFi 后
# 浏览器打开 http://<本机局域网IP>:8000 即可。
# 注意：iOS 真正“离线可装”的 PWA 需要 HTTPS（service worker 限制）。
# 仅本机/局域网测试 UI 用 HTTP 即可；要离线安装请托管到 GitHub Pages 等 HTTPS 静态空间。
import http.server, socketserver, os

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))

class H(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".webmanifest": "application/manifest+json",
        ".js": "text/javascript",
        ".png": "image/png",
    }
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)
    def log_message(self, *a):
        pass

with socketserver.TCPServer(("", PORT), H) as httpd:
    print(f"附点排课 PWA 预览: http://localhost:{PORT}  (Ctrl+C 停止)")
    httpd.serve_forever()
