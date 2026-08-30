import time
import random
import json
from instagrapi import Client

def load_accounts():
    """تحميل الحسابات من ملف accounts.json"""
    try:
        with open('accounts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ ملف accounts.json غير موجود!")
        return []
    except json.JSONDecodeError:
        print("❌ خطأ في صيغة ملف accounts.json!")
        return []

def follow_target(account, target_username):
    """حساب واحد يتابع الهدف"""
    try:
        cl = Client()
        print(f"🔐 جاري تسجيل الدخول بـ {account['username']}...")
        cl.login(account['username'], account['password'])
        
        print(f"🔍 جاري البحث عن {target_username}...")
        target_id = cl.user_id_from_username(target_username)
        
        print(f"➕ جاري متابعة {target_username}...")
        cl.user_follow(target_id)
        
        print(f"✅ {account['username']} تابع {target_username} بنجاح!")
        cl.logout()
        print(f"🚪 {account['username']} سجل الخروج")
        return True
    except Exception as e:
        print(f"❌ {account['username']} فشل: {e}")
        return False

def mass_follow():
    """تشغيل كل الحسابات"""
    print("=" * 50)
    print("🚀 INSTAGRAM MASS FOLLOWER TOOL")
    print("=" * 50)
    
    accounts = load_accounts()
    if not accounts:
        print("❌ لا توجد حسابات للعمل!")
        return
    
    print(f"📊 عدد الحسابات: {len(accounts)}")
    
    target = input("🎯 أدخل اسم المستخدم المستهدف: ").strip()
    if not target:
        print("❌ لم تدخل أي اسم!")
        return
    
    print("=" * 50)
    print(f"🎯 الهدف: {target}")
    print(f"📊 الحسابات: {len(accounts)}")
    print("=" * 50)
    
    success_count = 0
    for i, acc in enumerate(accounts, 1):
        print(f"\n🔄 [{i}/{len(accounts)}] تشغيل {acc['username']}...")
        
        if follow_target(acc, target):
            success_count += 1
        
        if i < len(accounts):
            wait_time = random.randint(60, 180)
            print(f"⏳ انتظر {wait_time} ثانية قبل الحساب التالي...")
            time.sleep(wait_time)
    
    print("=" * 50)
    print(f"✅ اكتمل! نجح {success_count} من {len(accounts)} حساب")
    print("=" * 50)

if __name__ == "__main__":
    mass_follow()