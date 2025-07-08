//romise yapısını daha okunabilir ve senkron gibi yazmamıza yarayan sözdizimidir.
async function getData() {
    const result = await fetchDataPromise();
    console.log(result); // 1 saniye sonra: "Promise resolved!"
  }
  
  getData();

  /**Açıklama:

    async fonksiyonlar Promise döner.

    await, bir Promise'in tamamlanmasını bekler.

    Kod, senkron gibi görünür, ama arkada asenkron çalışır.

    Daha okunabilir ve yönetilebilir */