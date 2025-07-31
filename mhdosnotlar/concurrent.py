from concurrent.futures import ThreadPoolExecutor, as_completed
##threadpoolexecuter parallel işlemler yapar as_completed ise sıralı verir
##her url çıktısını paralel olarak alır 
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
def fetch_url(url):
    response = requests.get(url) ##url ye get isteği gönderir
    return f"{url}: {response.status_code}"

urls = ["https://example.com", "https://python.org", "https://github.com"]
with ThreadPoolExecutor(max_workers=3) as executor: ##aynı anda çalışavak işçi sayısı
    futures = [executor.submit(fetch_url, url) for url in urls]
    for future in as_completed(futures):
        print(future.result())








