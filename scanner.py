import requests
import socket
from datetime import datetime

def print_banner():
    print("-" * 50)
    print("   🌐 SITE SECURITY SCANNER 🌐   ")
    print(f"   Created by: Emad (@jk.v.ip)  ")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

def scan_target(target):
    try:
        # 1. تحويل الرابط إلى IP
        hostname = target.replace("https://", "").replace("http://", "").split('/')[0]
        ip = socket.gethostbyname(hostname)
        print(f"[+] Target Host: {hostname}")
        print(f"[+] Target IP: {ip}")

        # 2. فحص استجابة السيرفر وتحديد نوعه
        response = requests.get(target, timeout=5)
        print(f"[+] Status Code: {response.status_code}")
        print(f"[+] Web Server: {response.headers.get('Server', 'Unknown')}")
        print(f"[+] Content Type: {response.headers.get('Content-Type')}")
        
        # 3. فحص بروتوكول الحماية SSL
        if target.startswith("https"):
            print("[+] Connection: Secure (HTTPS)")
        else:
            print("[!] Warning: Connection is not secure (HTTP)")

    except Exception as e:
        print(f"[-] Error: {str(e)}")

if __name__ == "__main__":
    print_banner()
    url = input("Enter Target URL (e.g., https://google.com): ")
    scan_target(url)
