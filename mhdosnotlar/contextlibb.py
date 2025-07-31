##try expect blouğunu daha temiz yazmak için
from contextlib import suppress
import os

with suppress(FileNotFoundError): ##dosya yoksa hata olmadan devam eder 
    os.remove("non_existent_file.txt")
print("Dosya silme denendi, hata olsa bile devam ediliyor.")