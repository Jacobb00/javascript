const fs = require('fs');
fs.readFile('file.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Dosya okunurken bir hata oluştu:', err);
        return;
    }
    console.log('Dosya içeriği:', data);
});






