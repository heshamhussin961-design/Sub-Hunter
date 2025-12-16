import requests
import sys
import concurrent.futures
import socket
from colorama import Fore, Style, init
from fake_useragent import UserAgent

# ---------------------------------------------------------
# Tool Name: Sub-Hunter v3.0 (Ghost Mode)
# Author: Cyber Man
# Description: Advanced Recon with IP resolution & Stealth
# ---------------------------------------------------------

# تفعيل الألوان في التيرمينال
init(autoreset=True)

# تجهيز التخفي (Random User Agents)
ua = UserAgent()

def banner():
    print(Fore.GREEN + Style.BRIGHT + """
    ____________________________________________________
      ____        _       _   _             _            
     / ___| _   _| |__   | | | |_   _ _ __ | |_ ___ _ __ 
     \___ \| | | | '_ \  | |_| | | | | '_ \| __/ _ \ '__|
      ___) | |_| | |_) | |  _  | |_| | | | | ||  __/ |   
     |____/ \__,_|_.__/  |_| |_|\__,_|_| |_|\__\___|_|   
                     v3.0 (GHOST MODE) 👻
    ____________________________________________________
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + "[*] Target Locked. Starting Stealth Scan..." + Style.RESET_ALL)
    print("-" * 60)

def get_ip(subdomain):
    """
    وظيفة جانبية تجيب الـ IP بتاع الدومين
    """
    try:
        return socket.gethostbyname(subdomain)
    except:
        return "Unknown"

def check_subdomain(domain, sub):
    full_url = f"http://{sub}.{domain}"
    full_domain = f"{sub}.{domain}"
    
    # كل طلب هيروح بـ User-Agent مختلف (تخفي)
    headers = {'User-Agent': ua.random}
    
    try:
        # timeout قليل عشان السرعة
        response = requests.get(full_url, headers=headers, timeout=1.5)
        
        if response.status_code == 200:
            ip_address = get_ip(full_domain)
            
            # طباعة النتيجة بشكل ملون ومنظم
            print(f"{Fore.GREEN}[+] FOUND: {Fore.WHITE}{full_domain.ljust(30)} {Fore.CYAN}[IP: {ip_address}]{Style.RESET_ALL}")
            
            # الحفظ في الملف
            with open("ghost_results.txt", "a") as f:
                f.write(f"{full_domain} : {ip_address}\n")
                
        elif response.status_code in [403, 401]:
            # لو الموقع شغال بس مانعنا (Forbidden)، ده كنز برضه!
            print(f"{Fore.YELLOW}[!] PROTECTED ({response.status_code}): {Fore.WHITE}{full_domain}")

    except requests.ConnectionError:
        pass
    except Exception:
        pass

def main():
    if len(sys.argv) < 3:
        print(Fore.RED + "Usage: python sub_hunter.py <domain> <wordlist>")
        sys.exit()

    target_domain = sys.argv[1]
    wordlist_file = sys.argv[2]
    
    subdomains = []
    try:
        with open(wordlist_file, "r") as file:
            subdomains = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(Fore.RED + "[Error] Wordlist file not found!")
        sys.exit()

    banner()

    # تشغيل 20 Thread عشان السرعة القصوى
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(check_subdomain, target_domain, sub) for sub in subdomains]
        
    print("-" * 60)
    print(Fore.GREEN + "[✓] Scan Completed. Results saved to 'ghost_results.txt'")

if __name__ == "__main__":
    main()