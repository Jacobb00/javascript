/**await, sadece async fonksiyonlar içinde kullanılır ve bir Promise’in sonucunu beklemek anlamına gelir.

Yani:

    "Bu işlem bitene kadar bekle, sonra devam et." */
    function veriGetir() {
        return new Promise(resolve => {
          setTimeout(() => {
            resolve('Veri geldi!');
          }, 2000);
        });
      }
      
      async function işle() {
        console.log('1. Veri bekleniyor...');
        const sonuc = await veriGetir(); // 2 saniye bekler
        console.log('2. Cevap:', sonuc);
      }
      
      işle();
      

      /**erçek Hayattan Benzerlik

Diyelim ki pizza siparişi verdin:

    Promise: Pizzacı "15 dakika içinde getiririm" diye söz veriyor.

    then(): Pizza gelirse “Afiyet olsun” diyorsun.

    catch(): Pizza gelmezse “Niye gelmedi?” diyorsun.

    async/await: Sen pizzayı bekliyorsun, sonra yemeye başlıyorsun. */ 