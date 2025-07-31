import dns.resolver
##dns sorgularını döndürür
cevap = dns.resolver.resolve("google.com", "A")
for ip in cevap:
    print(ip)
