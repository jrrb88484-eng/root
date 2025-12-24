import requests
import time

# إعدادات التنبيه (ضع بياناتك هنا)
TOKEN = "8339896091:AAFHQMx2aLaFAr0YSrly5Mw5t6u-OzLAn4I"
CHAT_ID = "6487654326"
HOST = "iq.zain.com" # الثغرة الناجحة

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(url)

print("🚀 السيرفر بدأ العمل على Railway...")
send_msg("✅ السيرفر يعمل الآن وبدأ فحص ثغرة زين.")

while True:
    try:
        # فحص استجابة الهوست
        response = requests.get(f"http://{HOST}", timeout=10)
        if response.status_code in [200, 301, 302]:
            print(f"🌐 {HOST} Is UP!")
        else:
            send_msg(f"⚠️ تنبيه: الثغرة تعطي استجابة {response.status_code}")
    except:
        print("❌ فشل في الوصول للهوست.. محاولة أخرى")
    
    time.sleep(60) # فحص كل دقيقة لتجنب الحظر
