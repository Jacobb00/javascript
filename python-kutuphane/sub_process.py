## nmap gobuster gibi araçlları komutları çağırabilirisin
#subprocess.run() — Komutu çalıştırır, tamamlanmasını bekler.

#subprocess.Popen() — Daha esnek, süreci başlatır, kontrol sağlar.

import subprocess

# Basit komut çalıştırma (örnek: ls -l)
result = subprocess.run(["ls", "-l"], capture_output=True, text=True) #çıktılar strıng olarak alınır tex=true da capture outputda standrat çktı ve errror bilgileri

print("Çıktı:")
print(result.stdout)

print("Hata varsa:")
print(result.stderr)

print("Çıkış kodu:", result.returncode)
