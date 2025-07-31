##regex ile metin armaa
import re

## Metinde sayıları bul
metin = "Yakup 25 yaşında ve 2 kardeşi var."
sonuclar = re.findall(r"\d+", metin)  ## \d+ = 1 veya daha fazla rakam
print(sonuclar)  ## ['25', '2']
