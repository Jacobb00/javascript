import os

## Geçerli çalışma dizinini al
print(os.getcwd())  ## Örn: C:\Users\Yakup

## Yeni klasör oluştur
os.mkdir("deneme_klasor")

## Dosya var mı kontrol et
print(os.path.exists("deneme_klasor"))  ## True
