from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios/{user_id}")
def obtener_usuario(user_id: int):
    return {
        "id": user_id,
        "nombre": "Sebas",
        "edad": 30
    }