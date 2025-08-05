## fonksiyona kaç tane arguman gönderileceği belli değilse
def sayilar(*args):
    toplam=0    
    for i in args:
        toplam+=i
    print(toplam)
sayilar(1,2,3,4,5,6,7,8,9,10)






