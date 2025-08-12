# main.py
from fastapi import FastAPI
##kolay bi şekilde restful apileri sağlar 

# FastAPI uygulaması oluştur
app = FastAPI()

# Ana sayfa endpoint
@app.get("/")
def read_root():
    return {"message": "Merhaba Yakup! FastAPI çalışıyor 🚀"}

# Parametre ile endpoint
@app.get("/merhaba/{isim}")
def read_item(isim: str):
    return {"mesaj": f"Merhaba {isim}!"}
## uvicorn main:app --reload uygulamayı çalıştırır
