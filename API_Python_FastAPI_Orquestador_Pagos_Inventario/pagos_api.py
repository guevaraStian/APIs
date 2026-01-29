import asyncio
from fastapi import FastAPI, HTTPException
from utils import guardar_json

app = FastAPI(title="API Pagos")

@app.post("/pagar")
async def pagar(monto: float, metodo: str):
    await asyncio.sleep(1)

    if metodo not in ["Stripe", "PayPal"]:
        raise HTTPException(status_code=400, detail="Método no soportado")

    data = {
        "monto": monto,
        "metodo": metodo,
        "estado": "aprobado"
    }

    guardar_json("BaseDeDatos/pagos", data)

    return data