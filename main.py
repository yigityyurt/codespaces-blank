import os
from fastapi import FastAPI

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "Gelistirme Ortami")

@app.get("/")
def read_root():
    return {"message": "Merhaba CENG413!", "environment": APP_ENV}

@app.get("/health")
def health_check():
    return {"status": "healthy"}