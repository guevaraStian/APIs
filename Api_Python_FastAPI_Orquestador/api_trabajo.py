# Se importan librerias
from fastapi import FastAPI

app = FastAPI()

@app.get("/trabajo/{user_id}")
def obtener_trabajo(user_id: int):
    return {
        "user_id": user_id,
        "Nombre_trabajo": 3000,
        "Descripcion": "Labores varias",
        "Fecha_ingreso": "20260101"
    }