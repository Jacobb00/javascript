## dunder metodları python için özel metotlardır
"""
__init__ → Nesne oluşturulurken çalışır.

__str__ → print() ile nesneyi yazdırdığında çağrılır.

__repr__ → Nesnenin "temsil" (representation) çıktısı.

__len__ → len() ile nesnenin uzunluğunu döndürür.

__getitem__ → obj[index] gibi erişim.

__call__ → Nesneyi fonksiyon gibi çağırma.

__add__ → + operatörünü özelleştirme.
"""
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"Kitap: {self.title} ({self.pages} sayfa)"
    
    def __len__(self):
        return self.pages
    
    def __add__(self, other):
        return self.pages + other.pages

book1 = Book("Python 101", 300)
book2 = Book("OOP Mastery", 250)

print(book1)        # Kitap: Python 101 (300 sayfa)
print(len(book1))   # 300
print(book1 + book2) # 550








