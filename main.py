import os
import http.server
import socketserver
import threading

# هذا الجزء لفتح المنفذ المطلوب من قبل Render
PORT = int(os.environ.get("PORT", 443))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Vmess Server is Live")

def run_web_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    # تشغيل السيرفر في خلفية لضمان عدم حدوث Timeout
    threading.Thread(target=run_web_server, daemon=True).start()
    
    # رسالة نجاح في السجلات
    print("🚀 V2Ray Vmess Bridge is active")
    
    # إبقاء الكود يعمل للأبد
    import time
    while True:
        time.sleep(100)
