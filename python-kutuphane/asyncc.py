#async: Fonksiyonun asenkron olduğunu belirtir.

#await: Uzun süren işlemi beklerken diğer işlerin devam etmesini sağlar.

## kısa süren işeri dahaa erken bititir

import asyncio

async def async_islem():
    print("Async işlem başladı")
    await asyncio.sleep(2)  # 2 saniye bekle (asenkron)
    print("Async işlem bitti")

async def main():
    print("Başladı")
    await async_islem()
    print("Bitti")

asyncio.run(main())
