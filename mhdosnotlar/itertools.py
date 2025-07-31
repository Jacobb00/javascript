## bir liste üzerinde sonsuz bi döngü oluşturur
from itertools import cycle

proxies = ["proxy1", "proxy2", "proxy3"] 
proxy_cycle = cycle(proxies)
for _ in range(5):  ##5 kere döndürür listeyi
    print(next(proxy_cycle))
    '''proxy1
proxy2
proxy3
proxy1
proxy2'''