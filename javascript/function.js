function selamla(){
    console.log("merhaba")
}
selamla();
const carpma =function(a,b){
    return a*b;
}
console.log(carpma(2,3));

const carp = (a, b) => { //arrow fonksiyonları daha kısa yazım sağlar . carp bir fonskiyondur
    return a * b;
  };
  
  console.log(carp(5, 6)); // 30

  const kare = x => x * x; //eğer sadece bir parametre varsa parantez kullanmaya gerek yok

console.log(kare(4)); // 16




///SCOPE
//Global Scope: Fonksiyon dışında tanımlanan değişkenler, her yerden erişilebilir.

//Local Scope: Fonksiyon içinde tanımlanan değişkenler sadece o fonksiyon içinde geçerlidir.

let globalDegisken = "Ben globalim";

function fonksiyon() {
  let localDegisken = "Ben yerelim";
  console.log(globalDegisken);  // Erişilebilir
  console.log(localDegisken);   // Erişilebilir
}

fonksiyon();

console.log(globalDegisken);    // Erişilebilir
 //console.log(localDegisken);  // Hata! Yerel değişkene dışarıdan erişilemez


 /*4. Hoisting (Yukarı Taşıma)

JavaScript, fonksiyon deklarasyonlarını ve var ile tanımlanan değişkenleri kodun en üstüne taşır (hoist eder).
 */
selamla1();

function selamla1() {
  console.log("Merhaba!");
}
//Bu kod hata vermez çünkü fonksiyon tanımı hoisted edilmiştir.
