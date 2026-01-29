import asyncio
from fastapi import FastAPI
from utils import guardar_json

app = FastAPI(title="API Notificaciones")

@app.post("/notificar")
async def notificar(mensaje: str, canal: str):
    await asyncio.sleep(0.3)

    data = {
        "mensaje": mensaje,
        "canal": canal,
        "estado": "enviado"
    }

    guardar_json("BaseDeDatos/notificaciones", data)

    return data
