##logları kaydeder
"""    :

        Programın çalışırken yaptığı işlemleri kaydetmek

        Hataları, uyarıları, bilgi mesajlarını saklamak

        Geliştirme ve hata ayıklamada çok faydalıdır

📌 Avantajı: print() gibi ekrana yazmaz sadece, dosyaya kaydedebilir, farklı seviyelerde log tutabilir.
ogging kütüphanesi mesajları önem derecesine göre kategorize eder:
Seviye	Anlamı
DEBUG	En ayrıntılı, hata ayıklama bilgileri
INFO	Genel bilgi mesajları
WARNING	Uyarılar
ERROR	Hatalar
CRITICAL	Çok ciddi hatalar
basicConfig()

    Loglama sisteminin temel ayarlarını yapar.

    Parametreler:

        level → Loglama seviyesi (DEBUG, INFO, vb.)

        format → Log mesajının biçimi

        filename → Logların yazılacağı dosya (yazmazsan konsola yazar)

        filemode → Dosya modu (w = üzerine yaz, a = ekle)"""
import logging

# Temel ayarlar
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="uygulama.log", ##bunları yazmazsan konsola yazar
    filemode="w"
)

# Logger oluştur
logger = logging.getLogger("AnaModul")

# Log mesajları
logger.debug("Bu debug mesajıdır")
logger.info("Program başladı")
logger.warning("Disk alanı azaldı")
logger.error("Dosya bulunamadı")
logger.critical("Sistem çöküyor!")

# Loglama sistemini kapat
logging.shutdown()
