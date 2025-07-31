import subprocess

## Komut çalıştır
sonuc = subprocess.run(["echo", "Merhaba Yakup"], capture_output=True, text=True)
print(sonuc.stdout)  ## Merhaba Yakup
