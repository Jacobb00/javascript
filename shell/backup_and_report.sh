#!/bin/bash 
##Bu script, belirli bir dizini (örneğin /home/yakup/important_data) sıkıştırıp yedekler, yedek dosyasını belirli bir dizine taşır, ardından işlemle ilgili bir log dosyası oluşturur ve eğer hata olursa e-posta ile uyarı gönderir.


#!/bin/bash

# 1. Değişken tanımlamaları
SOURCE_DIR="C:\Users\celik\OneDrive\Masaüstü\azurerm"
BACKUP_DIR="/backup"
LOG_FILE="/var/log/backup_$(date +'%Y-%m-%d').log"
EMAIL="yakup@example.com"

# 2. Tarih bilgisi (yedek dosyası için)
DATE=$(date +'%Y-%m-%d_%H-%M-%S')

# 3. Yedek dosyasının adı
BACKUP_FILE="backup_${DATE}.tar.gz"

# 4. Başlangıç mesajı log dosyasına yazılır
echo "Yedekleme başladı: $(date)" >> "$LOG_FILE"

# 5. Yedekleme işlemi (sıkıştırma)
tar -czf "${BACKUP_DIR}/${BACKUP_FILE}" -C "$SOURCE_DIR" .

# 6. Yedekleme durumunu kontrol et
if [ $? -eq 0 ]; then
    echo "Yedekleme başarılı: ${BACKUP_FILE}" >> "$LOG_FILE"
else
    echo "Yedekleme başarısız!" >> "$LOG_FILE"
    mail -s "Yedekleme Hatası" "$EMAIL" <<< "Sistem yedekleme işlemi başarısız oldu. Lütfen kontrol ediniz."
    exit 1
fi

# 7. Eski yedekleri 7 gün sonra sil
find "$BACKUP_DIR" -name "backup_*.tar.gz" -type f -mtime +7 -exec rm {} \;

# 8. Bitiş mesajı log dosyasına yazılır
echo "Yedekleme tamamlandı: $(date)" >> "$LOG_FILE"
