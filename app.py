from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from uuid import uuid4 as uuid
import uvicorn

app = FastAPI()

posts = []

class Post(BaseModel):
    Nombre: str
    Fecha: str
    Comentario: str

@app.get('/')
def read_root():
    return {"Bienvenidos": "Bienvenidos a mi proyecto final API"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="La pelicula no existe")

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "La pelicula ha sido eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="La pelicula no existe")

@app.put('/posts/{post_id}')
def update_post(post_id: str, updatedPost: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["Nombre"]= updatedPost.dict()["Nombre"]
            posts[index]["Fecha"]= updatedPost.dict()["Fecha"]
            posts[index]["Comentario"]= updatedPost.dict()["Comentario"]
           
            return {"message": "La pelicula se ha actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="La pelicula no existe")