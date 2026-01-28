# API PYTHON FASTAPI, CRUD pero se requieren las siguientes librerias
# pip install fastapi
# pip install uvicorn
# Para que funcione la aplicacion hay que ejecutar el siguiente comando
# uvicorn app:app
# http://127.0.0.1:8000/docs 

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4 as uuid
from typing import Optional, Text

app = FastAPI()

publicaciones = []

class publicacion(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime] = None
    published: bool = False

class publicacionUpdate(BaseModel):
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()

@app.get('/')
def read_root():
    return {'title': 'Inicio de una API python .'}

@app.get('/publicaciones')
def get_publicaciones():
    return publicaciones

@app.post('/publicaciones/crear')
def create_post(publicacion:publicacion):
    publicacion.id = str(uuid())
    publicaciones.append(publicacion.dict())
    return {'message':'publicacion creada satisfactoriamente'}

@app.get('/publicaciones/{id_publicacion}')
def get_post_by_id(id_publicacion:str):
    for publicacion in publicaciones:
        if publicacion['id'] == id_publicacion:
            return publicacion
    raise HTTPException(status_code=404, detail='Publicacion no encontrada')

@app.delete('/publicaciones/eliminar/{id_publicacion}')
def delete_post(id_publicacion:str):
    for index, publicacion in enumerate(publicaciones):
        if publicacion['id'] == id_publicacion:
            publicaciones.pop(index)
            return {'message':'Publicacion eliminada correctamente'}
    raise HTTPException(status_code=404, detail='Publicacion no encontrada')

@app.put('/publicaciones/editar/{id_publicacion}')
def update_post(id_publicacion:str, updatedPost:publicacionUpdate):
    for publicacion in publicaciones:
        if publicacion['id'] == id_publicacion:
            publicacion.update(updatedPost.dict())
            return {'message':'Publicacion actualizada correctamente'}
    raise HTTPException(status_code=404, detail='Publicacion no encontrada')


