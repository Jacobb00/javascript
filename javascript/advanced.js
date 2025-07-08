/**1. Callback Fonksiyonlar

Bir fonksiyonun parametre olarak başka bir fonksiyon alması durumudur. İş bittikten sonra çağrılı */

function selamla(ad, callback) {
    console.log("Merhaba " + ad);
    callback(); // işlem sonrası çalıştırılır
  }
  
  selamla("Ahmet", function() {
    console.log("Fonksiyon tamamlandı.");
  });

  /** 2. Promises (Sözler)

Asenkron işlemleri daha yönetilebilir hale getirir. Üç durumu vardır:

    pending (beklemede)

    fulfilled (başarılı)

    rejected (başarısız) */

    let soz = new Promise((resolve, reject) => {
        let durum = true;
        if (durum) {
          resolve("İşlem başarılı");
        } else {
          reject("Bir hata oluştu");
        }
      });
      
      soz
        .then(sonuc => console.log(sonuc))
        .catch(hata => console.log(hata));
      
  