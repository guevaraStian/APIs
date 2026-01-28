pip install fastapi uvicorn requests
uvicorn api_usuarios:app --port 8001 --reload
uvicorn api_contabilidad:app --port 8002 --reload
uvicorn api_trabajo:app --port 8003 --reload
uvicorn orquestador:app --port 8000 --reload

GET http://localhost:8001/usuario/1
GET http://localhost:8002/contabilidad/1
GET http://localhost:8002/trabajo/1
GET http://localhost:8000/perfil-completo/1