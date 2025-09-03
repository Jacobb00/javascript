from celery_test import add

# Görevi asenkron olarak çalıştır
result = add.delay(5, 7)  # delay() görevleri kuyruğa ekler

# Sonucu bekle ve al"""
print(result.get(timeout=10))  # 12
"""celery -A tasks worker --loglevel=info
-A tasks → Celery uygulamasının tanımlı olduğu dosya.

worker → Arka plan çalışanını başlatır.

--loglevel=info → Log detayını gösterir."""