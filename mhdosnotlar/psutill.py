import psutil
 ##sistem bilgileri
print(psutil.cpu_count())              ## CPU sayisi
print(psutil.cpu_count(logical=False)) ## CPU sayisi
print(psutil.cpu_times())              ## CPU kullanımı     
print(psutil.cpu_percent(interval=1))  ## CPU kullanımı
print(psutil.virtual_memory())         ## RAM bilgisi
