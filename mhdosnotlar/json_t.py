##json key-value yapısına sahiptir ve veri saklar
import json  # JSON kütüphanesini içe aktarıyoruz

# 1. JSON dosyasını aç
with open("data.json", "r", encoding="utf-8") as dosya:
    # 2. JSON verisini Python'a çevir
    veri = json.load(dosya)

# 3. Artık veri bir Python sözlüğü
print(veri)
print(type(veri))       # <class 'dict'>
print(veri["isim"])     # Yakup
print(veri["hobiler"])  # ['müzik', 'siber güvenlik', 'yazılım']
