let meyveler = ["elma", "armut", "muz"];
meyveler.push("çilek");  // sona ekler
console.log(meyveler);   // ["elma", "armut", "muz", "çilek"]

meyveler.pop();          // sondaki elemanı çıkarır
console.log(meyveler);   // ["elma", "armut", "muz"]


let uzunluklar = meyveler.map(meyve => meyve.length); //map dizi içindeki elemanların uzunluğunu alır her elemana uygulanır

console.log(uzunluklar); // [4, 5, 3]

let uzunMeyveler = meyveler.filter(meyve => meyve.length > 4); //filter koşula uyanları alır
console.log(uzunMeyveler); // ["armut"]
meyveler.forEach(meyve => console.log(meyve)); //her elemanı yazdırır 


//objects
 let kisi ={
    isim: "yakup",
    yas: 20,
    meslek:"yazılımcı"
 }
 console.log(kisi.isim);
 console.log(Object.keys(kisi)); //objenin keysini yazıdır
 console.log(Object.values(kisi)); //objenin valuesini yazdırı