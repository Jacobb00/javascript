from celery import Celery

# Celery uygulamasını oluştur
app = Celery('my_app', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Basit bir görev tanımla
@app.task
def add(x, y):
    return x + y
