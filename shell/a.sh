#!/bin/bash

echo "Hello, World!"

isim="John"
echo "Merhaba, $isim!" # dolar işareti ile değişken atanur


echo "isim gir"
read isim # input bekler
echo "Merhaba, $isim!"



echo "bir sayı gir"
read sayi 
if [ $sayi -gt 10 ]; then ##if ile parantez arasında BOŞLUK olmalı duyarlo  -lt less than -eq equa
 echo "sayı 10'dan büyük"
else
 echo "sayı 10'dan küçük"
fi

for i in 1 2 3 4 5; do
 echo "sayı $i"   #her bir sayıyı yazdırır
done







echo "bir sayı gir"