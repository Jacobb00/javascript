import threading

def yaz():
    print("Merhaba Yakup")

t = threading.Thread(target=yaz)
t.start()
t.join()
