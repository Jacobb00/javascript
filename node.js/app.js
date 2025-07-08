let http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World!');
}).listen(8080);  //8080 portu açılır

console.log('This example is different!'); //terminalde görünür sadece
console.log('The result is displayed in the Command Line Interface'); 
const os = require('os');  //os modülünü built in kullandı 
/*Dosya işlemleri yapmak (fs)

    İşletim sistemi bilgisi almak (os)

    HTTP sunucusu kurmak (http)

    Dosya yollarıyla çalışmak (path) */
console.log(os.platform());  //burda da os u print ediyor

// const constant sabit değiştirilemeyen atamalarda yapılır
const express = require('express'); //exporess modulunu kullandık 
const app = express();
app.get('/', (req, res) => res.send('Hello World333!'));
app.listen(8081);
