import asyncio
from fastapi import FastAPI
from utils import guardar_json

app = FastAPI(title="API Facturación")

@app.post("/facturar")
async def facturar(producto: str, cantidad: int, envio: float, total: float):
    await asyncio.sleep(0.5)

    data = {
        "producto": producto,
        "cantidad": cantidad,
        "envio": envio,
        "total": total
    }

    guardar_json("BaseDeDatos/facturacion", data)

    return data