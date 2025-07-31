#!/bin/bash

function selamla {
 echo "Merhaba, $1!"  ##dolar bir fonksiyona verilen parametreyi yazdırır
}

selamla "John"



if [ -f "read.txt" ]; then  ## dizin için -d kullanılır
 echo "read.txt dosyası var"
else
 echo "read.txt dosyası yok"
fi


echo "Toplam argüman sayısı: $#"
echo "Birinci argüman: $1"



