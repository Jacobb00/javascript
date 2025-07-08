try {
    let x = y + 1; // y tanımlı değil, hata fırlatır
  } catch (err) {
    console.log("Hata yakalandı:", err.message);
  }
  
  function yasKontrol(yas) {
    if (yas < 18) {
      throw new Error("18 yaşından küçükler giriş yapamaz.");
    }
    return "Giriş başarılı!";
  }
  
  try {
    console.log(yasKontrol(16));
  } catch (e) {
    console.log("Hata:", e.message);  // 18 yaşından küçükler giriş yapamaz.
  }
  

  /**arayıcı Geliştirici Araçları (F12)

    Console sekmesi: console.log, console.error, console.warn mesajlarını gösterir.

    Sources sekmesi: Kodları adım adım izlemek, breakpoint koymak için kullanılır.

    Network sekmesi: API çağrılarının başarılı olup olmadığını kontrol etmek için.
     */