import asyncio
from fastapi import FastAPI, HTTPException
from data import ENVIOS
from utils import guardar_json

app = FastAPI(title="API Envíos")

@app.get("/calcular")
async def calcular(empresa: str):
    await asyncio.sleep(0.5)

    if empresa not in ENVIOS:
        raise HTTPException(status_code=400, detail="Empresa no válida")

    data = {
        "empresa": empresa,
        "costo": ENVIOS[empresa]
    }

    guardar_json("BaseDeDatos/envios", data)

    return data