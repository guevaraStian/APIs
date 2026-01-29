pip install fastapi uvicorn requests



uvicorn pagos_api:app --port 8001


uvicorn inventario_api:app --port 8002


uvicorn envios_api:app --port 8003


uvicorn facturacion_api:app --port 8004


uvicorn notificaciones_api:app --port 8005


uvicorn main:app --port 8000


http://localhost:8001/docs
curl -X POST "http://localhost:8001/pagar?monto=1000&metodo=Stripe"


http://localhost:8002/docs
curl -X POST "http://localhost:8002/reservar?producto_id=p1&cantidad=2"


http://localhost:8003/docs
curl "http://localhost:8003/calcular?empresa=DHL"


http://localhost:8004/docs
curl -X POST "http://localhost:8004/facturar?producto=Laptop&cantidad=2&envio=20&total=2020"


http://localhost:8005/docs
curl -X POST "http://localhost:8005/notificar?mensaje=Compra%20Exitosa&canal=WhatsApp"


http://localhost:8000/docs
curl -X POST "http://localhost:8000/comprar?producto_id=p1&cantidad=2&metodo_pago=Stripe&empresa_envio=DHL&canal_notificacion=WhatsApp"

