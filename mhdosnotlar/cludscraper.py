import cloudscraper
## cloudfare atlatmak için ama otomatik capchta kullanmaz
# Cloudscraper örneği oluştur
scraper = cloudscraper.create_scraper()

# Cloudflare korumalı bir siteye istek gönder
url = "https://elektraweb.com.tr"
response = scraper.get(url)

# Yanıtı kontrol et
if response.status_code == 200:
    print("Başarılı:", response.text)
else:
    print("Hata:", response.status_code)