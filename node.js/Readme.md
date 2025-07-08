node.js non blocking kullanır yani yüksek trafikte asenkron işlem yapabilir
Node.js, bazı önemli işlevler için hazır olarak gelen (yerleşik) modüllerle birlikte gelir. Bunlara “core modules” ya da “built-in modules” denir.

Bu modülleri ekstra yüklemeden doğrudan kullanabilirsin. Örneğin:

    Dosya işlemleri yapmak (fs)

    İşletim sistemi bilgisi almak (os)

    HTTP sunucusu kurmak (http)

    Dosya yollarıyla çalışmak (path)

const modulAdi = require('modulAdi');
