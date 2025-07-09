async function örnek() {
    return 'Merhaba';
  }
//Bu fonksiyonun dönüşü bir Promise olur. Şöyle kullanılır:
  örnek().then(cevap => {
    console.log(cevap); // "Merhaba"
  });
  