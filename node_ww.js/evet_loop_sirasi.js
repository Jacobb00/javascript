console.log('First');
setTimeout(() => console.log('Third'), 0);
Promise.resolve().then(() => console.log('Second'));
console.log('Fourth');

/** Event Loop Nasıl Çalışır?

Node.js aşağıdaki sırayla işlemleri yürütür:

    Ana senaryoyu çalıştırır (senkron kodlar)

    Microtask'ları işler (Promise, process.nextTick)

    Zamanlayıcıları çalıştırır (setTimeout, setInterval)

    I/O geri çağırmalarını çalıştırır (dosya, ağ işlemleri)

    setImmediate ile tanımlı görevleri çalıştırır

    Kapanış olaylarını işler (socket.on('close') gibi)Neden bu sırayla çalıştı?

    First ve Fourth: Senkron kod olduğu için hemen çalışır.

    Second: Promise ile tanımlanmış, bu bir microtask. Ana koddan sonra, diğer işlerden önce çalışır.

    Third: setTimeout ile tanımlandığı için, timer phase'da çalışır. */