##dosya yollarını nesne tabanlı yönetmek için 
from pathlib import Path

## Geçerli klasör yolunu al
p = Path.cwd()
print(p)

## Dosya oluştur
(Path("test.txt")).write_text("Merhaba Yakup!")

## Dosya var mı kontrol et
print(Path("test.txt").exists())  ## True
