##binary veri  paketleme ve açma
import struct

## Sayıyı 4 byte olarak paketle
data = struct.pack("i", 42)  ## i = int ## sayı 42 idir
print(data)

## Byte'ı tekrar aç
num = struct.unpack("i", data)[0]
print(num)
