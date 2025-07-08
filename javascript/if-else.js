let yas = 18;

if (yas >= 18) {
  console.log("Reşitsiniz.");
}


let gun = "Pazartesi";

switch(gun) {
  case "Pazartesi":
    console.log("Haftaya başlıyoruz.");
    break; //break yazmazsak diğer case leri de çalıştırır
  case "Cuma":
    console.log("Hafta sonu yaklaşıyor.");
    break;
  default:
    console.log("Bugün sıradan bir gün.");
}
for(let i=0;i<3;i++){
    console.log(i);
}

let j=0;
while(j<1){
    console.log(j);
    j++;
}

let meyveler = ["elma", "armut", "muz"]; 

for(let meyve of meyveler) { //for of diziler için kullanılır
  console.log(meyve);
}
let kisi = {isim: "Ali", yas: 30};

for(let key in kisi) { // for in objeler için kullanılır  yukarıda obje tanımladık
  console.log(key, ":", kisi[key]);
}

