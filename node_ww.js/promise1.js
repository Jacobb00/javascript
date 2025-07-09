const myPromise = new Promise((resolve, reject) => {
    resolve('Veri geldi!');
  });
  
  myPromise.then(data => {
    console.log(data); // "Veri geldi!" yazdırılır
  });
  const myPromise1 = new Promise((resolve, reject) => {
    reject('Bir hata oluştu!');
  });
  
  myPromise1
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.log('Hata:', error); // "Hata: Bir hata oluştu!"
    });
    /**Metot	Ne yapar?
.then()	resolve ile dönen sonucu alır.
.catch()	reject ile dönen hatayı yakalar. */
  