const myPromise = new Promise((resolve, reject) => {
    const success = true;
    if (success) {
        resolve('Veri geldi!');
    } else {
        reject('Bir hata oluştu!');
    }
});

myPromise.then(veri => {
    console.log(veri); // "Veri geldi!" yazdırılır
});