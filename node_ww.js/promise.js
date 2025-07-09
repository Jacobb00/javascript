//Promise (söz), gelecekte bir değerle sonuçlanacak veya hata verecek bir işlemi temsil eder.
const fetchDataPromise = () => {
    return new Promise((resolve) => {
      setTimeout(() => resolve('Promise resolved!'), 1000);
    });
  };
  
  fetchDataPromise().then(data => {
    console.log(data); // 1 saniye sonra: "Promise resolved!"
  });
/**Açıklama:

    Promise, iki parametre alır: resolve (başarı) ve reject (hata).

    setTimeout ile gecikmeli olarak resolve çağrılır.

    .then() ile sonucu alırız.

    .catch() ile hata yakalayabiliriz (örnek kodda yok ama mümkündür). */  