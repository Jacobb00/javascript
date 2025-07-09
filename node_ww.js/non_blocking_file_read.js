const fs = require('fs');

console.log('Dosya okunmadan önce');
fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log('Dosya içeriği:', data);
});
console.log('Dosya okuma çağrısından sonra'); //burda node.js dosya okuma ağır olduğu için hafif olanları hemen işler


const data = fs.readFileSync('file.txt', 'utf8'); // Tüm işlemi durdurur sonra aşağıdaki okunu r
console.log('Dosya okundu');

