# Bir liste oluşturalım
my_list = [1, 2, 3]

# Listeden bir iterator oluşturalım
my_iter = iter(my_list)  # __iter__() metodu çağrılır

# next() ile tek tek elemanları alalım
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3

# Artık eleman kalmadı
# print(next(my_iter))  # StopIteration hatası
