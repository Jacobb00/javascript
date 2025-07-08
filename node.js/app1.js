//npm init -y npm node.js için paket yönetimi için kullanılır
console.log("Hello World");
const http = require('http');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Merhaba, bu benim ilk Node.js sunucum!\n');
});

const port = 3000;
server.listen(port, () => {
  console.log(`Sunucu http://localhost:${port} adresinde çalışıyor`);
});

const {topla, cikar} = require('./utils');
console.log(topla(1, 2));
console.log(cikar(1, 2));