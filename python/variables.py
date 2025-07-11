x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0    bu casting oluyor o değerde olsun isiyoruz

"""
Pack" ve "Unpack" Nedir?
✅ Packing (Paketleme)

Verileri bir koleksiyon (liste, demet/tuple, vb.) içinde toplamak.
✅ Unpacking (Paket Açma)

Bir koleksiyon içindeki verileri tek tek değişkenlere ayırmak."""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)    ##cherry yazar

"""Bonus: * ile fazla verileri toplamak"""
fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]
x, y, *z = fruits
print(x)
print(y)
print(z)    ##[ cherry 'strawberry', 'raspberry'] yazar


xx=5
yy="john"
print(xx,yy) ##x+y deseydik hata verirdi



##global variables
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 





