"""Python’da .join() metodu stringlere ait bir metottur.
Bir liste ya da iterable (örneğin: list, tuple, set) içindeki elemanları tek bir string haline getirir.
Ama şunu unutma: .join() çalışabilmesi için listedeki elemanların hepsi string olmalı.
"ayırıcı".join(liste)
"ayırıcı" → Hangi karakteri araya koymak istediğini söylersin (örn: boşluk " ", virgül ",", tire "-", yeni satır "\n").

liste → Stringlerden oluşan bir liste ya da tuple."""

liste = ["ali", "veli", "ayşe", "ahmet"]
print("\n".join(liste)) ##yeni satır ile birleştirmedir bu 
