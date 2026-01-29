import asyncio
import httpx
from fastapi import FastAPI, HTTPException
from data import PRODUCTOS
from utils import guardar_json

app = FastAPI(title="Orquestador E-commerce")

@app.post("/comprar")
async def comprar(
    producto_id: str,
    cantidad: int,
    metodo_pago: str,
    empresa_envio: str,
    canal_notificacion: str
):
    async with httpx.AsyncClient() as client:
        try:
            producto = PRODUCTOS.get(producto_id)
            if not producto:
                raise HTTPException(status_code=404, detail="Producto no encontrado")

            subtotal = producto["precio"] * cantidad

            await client.post(
                "http://localhost:8001/pagar",
                params={"monto": subtotal, "metodo": metodo_pago}
            )

            await client.post(
                "http://localhost:8002/reservar",
                params={"producto_id": producto_id, "cantidad": cantidad}
            )

            envio = await client.get(
                "http://localhost:8003/calcular",
                params={"empresa": empresa_envio}
            )
            costo_envio = envio.json()["costo"]

            total = subtotal + costo_envio

            factura = await client.post(
                "http://localhost:8004/facturar",
                params={
                    "producto": producto["nombre"],
                    "cantidad": cantidad,
                    "envio": costo_envio,
                    "total": total
                }
            )

            asyncio.create_task(
                client.post(
                    "http://localhost:8005/notificar",
                    params={
                        "mensaje": f"Compra exitosa por ${total}",
                        "canal": canal_notificacion
                    }
                )
            )

            guardar_json("BaseDeDatos/orquestador", {
                "producto_id": producto_id,
                "cantidad": cantidad,
                "total": total
            })

            return {
                "estado": "COMPRA COMPLETADA",
                "factura": factura.json()
            }

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))