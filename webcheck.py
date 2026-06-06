#!/usr/bin/python
import requests
from colorama import Fore, Style, init
import time
import os

init(autoreset=True)

def notif(title, text):
    os.system(f'termux-notification --title "{title}" --content "{text}"')

def cek_website(url):
    if not url.startswith("http"):
        url = "https://" + url
    try:
        start = time.time()
        r = requests.get(url, timeout=10)
        waktu = round(time.time() - start, 2)
        if r.status_code == 200:
            print(f"{Fore.GREEN}[OK] {url} - Online | {waktu}s")
            return True
        else:
            print(f"{Fore.YELLOW}[!] {url} - Status {r.status_code}")
            notif("Website Warning", f"{url} return status {r.status_code}")
            return False
    except:
        print(f"{Fore.RED}[X] {url} - Offline")
        notif("Website DOWN!", f"{url} tidak bisa diakses")
        return False

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}=== Website Auto Monitor ==={Style.RESET_ALL}")
    url = input("Masukkan domain: ")
    interval = int(input("Cek tiap berapa detik? [300 = 5 menit]: ") or 300)
    print(f"\n{Fore.CYAN}Mulai monitoring {url} tiap {interval} detik...")
    print("Tekan Ctrl+C buat berhenti\n")
    try:
        while True:
            cek_website(url)
            time.sleep(interval)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Monitoring dihentikan")
