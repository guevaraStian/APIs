import asyncio
from fastapi import FastAPI, HTTPException
from data import PRODUCTOS
from utils import guardar_json

app = FastAPI(title="API Inventario")

@app.post("/reservar")
async def reservar(producto_id: str, cantidad: int):
    await asyncio.sleep(0.5)

    producto = PRODUCTOS.get(producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no existe")

    if producto["stock"] < cantidad:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    producto["stock"] -= cantidad

    data = {
        "producto_id": producto_id,
        "cantidad": cantidad,
        "stock_restante": producto["stock"]
    }

    guardar_json("BaseDeDatos/inventario", data)

    return data