#!/bash
echo "[+] Install dependensi..."
pkg update -y
pkg install python termux-api -y
pip install requests colorama

echo "[+] Download script..."
curl -s https://raw.githubusercontent.com/semb-commits/webcheck-tool/main/webcheck.py -o webcheck.py

echo "[+] Selesai! Jalanin dengan: python webcheck.py"
