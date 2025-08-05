## java daki this gibi sınıf içindeki nesnelere erişmek için kullanılır
## her sınıfın normal metodları kendi içinde self kullanmak zorunda self ismi öylesine yazılmış

class car:
    def __init__(self,brand,model,year):  ##yeni bi nesne oluşturulduğunda çalışır bu 
        self.brand = brand ##self ile bağlanılmazsa lokalde kalır sadece hata verir
        self.model = model ## dışardan gönderilen değerler self ile sınıfın içinde kullanılır
        self.year = year
    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
car1=car("BMW","X5",2020)
car2=car("Mercedes","C180",2021) ##python boş bir car nesnesi oluşturur ardından init metodunu çalıştırır
##__init__(car1,BMW,X5,2020) şeklinde değerler atar
car1.show_info()
car2.show_info()



##self parametre olarak otomatik mi gelir evet
class test:
    def hello(self):
        print("hello aaauu")
jacob=test()
jacob.hello()








