"""Python has the following data types built-in by default, in these categories:
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType"""


# Temel veri türleri örnekleri

x_str = "Hello World"                        # str: Metinsel veri (string)
x_int = 20                                   # int: Tam sayı (integer)
x_float = 20.5                               # float: Ondalıklı sayı
x_complex = 1j                               # complex: Karmaşık sayı (1 sanal sayı birimi)
x_list = ["apple", "banana", "cherry"]       # list: Değiştirilebilir, sıralı veri koleksiyonu
x_tuple = ("apple", "banana", "cherry")      # tuple: Değiştirilemez, sıralı veri koleksiyonu
x_range = range(6)                           # range: 0'dan 5'e kadar sayı üretir (0,1,2,3,4,5)
x_dict = {"name": "John", "age": 36}         # dict: Anahtar-değer (key-value) eşleşmesi
x_set = {"apple", "banana", "cherry"}        # set: Sırasız ve benzersiz öğelerden oluşur
x_frozenset = frozenset({"apple", "banana", "cherry"})  # frozenset: set gibi ama değiştirilemez
x_bool = True                                # bool: Mantıksal değer (True veya False)
x_bytes = b"Hello"                           # bytes: Değiştirilemez byte dizisi
x_bytearray = bytearray(5)                   # bytearray: Değiştirilebilir byte dizisi (5 adet sıfır byte içerir)
x_memoryview = memoryview(bytes(5))          # memoryview: Byte verisine doğrudan erişim sağlar
x_none = None                                # NoneType: Değeri olmayan nesne (boş anlamında)

# Her birinin veri türünü ekrana yazdıralım
print(type(x_str))         # <class 'str'>
print(type(x_int))         # <class 'int'>
print(type(x_float))       # <class 'float'>
print(type(x_complex))     # <class 'complex'>
print(type(x_list))        # <class 'list'>
print(type(x_tuple))       # <class 'tuple'>
print(type(x_range))       # <class 'range'>
print(type(x_dict))        # <class 'dict'>
print(type(x_set))         # <class 'set'>
print(type(x_frozenset))   # <class 'frozenset'>
print(type(x_bool))        # <class 'bool'>
print(type(x_bytes))       # <class 'bytes'>
print(type(x_bytearray))   # <class 'bytearray'>
print(type(x_memoryview))  # <class 'memoryview'>
print(type(x_none))        # <class 'NoneType'>
