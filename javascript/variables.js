var a = 5;
let b = 10;
const c = 15;

console.log(a, b, c); // 5 10 15

b = 20;   // let ile tanımlandığı için değiştirilebilir
// c = 25; // Hata! const ile tanımlanmış, değiştirilemez var kullanımı artık önerilmiyor

let isim = "Ahmet";          // String
let yas = 30;                // Number
let evliMi = false;          // Boolean
let bosDeger = null;         // Null
let tanimsiz;                // Undefined
let kisi = { isim: "Ali", yas: 25 };  // Object
let sayilar = [1, 2, 3, 4];            // Array
// null ve undefined farklıdır; null bilinçli olarak boş bırakılan, undefined ise tanımlanmamış anlamında.
let cc = 5;
let d = '5';

console.log(cc== d);  // true, çünkü == sadece değerleri karşılaştırır, tip önemsenmez
console.log(cc === d); // false, çünkü === hem değer hem de tip karşılaştırır, burada tipler farklı (number ve string)

