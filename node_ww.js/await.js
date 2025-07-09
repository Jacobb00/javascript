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
      