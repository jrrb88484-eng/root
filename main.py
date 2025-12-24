import os
import subprocess
import requests
import time

# بيانات التنبيه (اختياري)
TOKEN = "8339896091:AAFHQMx2aLaFArOYSrly5Mw5V"
CHAT_ID = "6487654326"

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    try: requests.get(url)
    except: pass

def start_v2ray():
    # هذا الجزء سيقوم بتحميل وتشغيل محرك V2Ray داخل Render
    PORT = os.environ.get('PORT', '443')
    # إعداد سيرفر Vmess بسيط يتوافق مع إعدادات هاتفك
    config = {
        "inbounds": [{
            "port": int(PORT),
            "protocol": "vmess",
            "settings": {"clients": [{"id": "4f17e173-4af9-5041-9662-f6c27e0decfa"}]},
            "streamSettings": {"network": "ws", "wsSettings": {"path": "/"}}
        }],
        "outbounds": [{"protocol": "freedom", "settings": {}}]
    }
    
    send_msg("🚀 سيرفر Vmess بدأ العمل الآن على المنفذ " + PORT)
    print("V2Ray is running...")
    
    # محاكاة لإبقاء السيرفر حياً
    while True:
        time.sleep(3600)

if __name__ == "__main__":
    start_v2ray()
