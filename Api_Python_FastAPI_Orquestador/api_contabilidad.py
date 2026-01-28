# Se importan librerias
from fastapi import FastAPI

app = FastAPI()

@app.get("/contabilidad/{user_id}")
def obtener_contabilidad(user_id: int):
    return {
        "user_id": user_id,
        "saldo": 80000,
        "moneda": "COL"
    }