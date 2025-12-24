import requests
import time
import http.server
import socketserver
import os
import threading

# بياناتك كما هي في الكود السابق
TOKEN = "8339896091:AAFHQMx2aLaFArOYSrly5Mw5V" 
CHAT_ID = "6487654326"
HOST = "iq.zain.com"

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    try: requests.get(url)
    except: pass

def checker():
    print("🚀 السيرفر بدأ فحص الثغرة...")
    send_msg("✅ السيرفر يعمل وبدأ فحص الثغرة الآن")
    while True:
        try:
            response = requests.get(f"http://{HOST}", timeout=10)
            print(f"🌐 {HOST} Is UP!")
        except:
            print("❌ محاولة فحص أخرى...")
        time.sleep(60)

# الجزء السحري لفتح منفذ Render (Port 10000)
PORT = int(os.environ.get("PORT", 10000))
def run_web_server():
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    # تشغيل خادم الويب في الخلفية لإبقاء الخدمة Live
    threading.Thread(target=run_web_server, daemon=True).start()
    # تشغيل الفاحص الخاص بك
    checker()
