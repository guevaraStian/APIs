# El siguiente software orquestador de diferentes API con la libreria fastapi
# el software agrupa diferentes apis en 1 sola llamada orquestador
# Usando la librerias cv2, numpy y dlib y sus datos
# En el terminal de comandos importar librerias con el comando PIP 
# pip install fastapi
# pip 25.1.1
# Python 3.13.1

from fastapi import FastAPI
import requests

app = FastAPI()

API_USUARIOS = "http://localhost:8001/usuarios"
API_CONTABILIDAD = "http://localhost:8002/contabilidad"
API_TRABAJO = "http://localhost:8003/trabajo"

@app.get("/perfil-completo/{user_id}")
def obtener_perfil_completo(user_id: int):
    
    usuario_resp = requests.get(f"{API_USUARIOS}/{user_id}")
    contabilidad_resp = requests.get(f"{API_CONTABILIDAD}/{user_id}")
    trabajo_resp = requests.get(f"{API_TRABAJO}/{user_id}")

    if usuario_resp.status_code != 200 or contabilidad_resp.status_code != 200 or trabajo_resp.status_code != 200:
        return {"error": "No se pudo obtener la información"}

    return {
        "Usuario": usuario_resp.json(),
        "contabilidad": contabilidad_resp.json(),
        "Trabajo": trabajo_resp.json()
    }