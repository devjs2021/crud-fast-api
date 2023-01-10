from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid1 as uaid


app = FastAPI()

class Post(BaseModel):
    id: Optional[str]
    title: str
    autor: str
    content: Text
    creando_en: datetime = datetime.now()
    publicado_en: Optional[datetime]
    publicado: bool = False

posts = []

@app.get("/")
async def hello():
    return {"Bienvenido":"Bienvenido"}

@app.get("/posts")
async def ger_post():
    return posts

@app.post("/posts")
async def save_post(post: Post):
        post.id = str(uaid())
        posts.append(post.dict())
        return posts[-1]

@app.post("/posts/{post_id}")
async def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post

    raise HTTPException(status_code=404, detail="Post Not Found")

@app.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)

            return "la publicacion se elimino correcto"
    
    raise HTTPException(status_code=404, detail="NOT FOUND ")

@app.put("/posts/{post_id}")
async def actualizar_post(post_id: str, update_post: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"] = update_post.title
            posts[index]["autor"] = update_post.autor
            posts[index]["content"] = update_post.content
            return {"message":"se actulizo de manera correcta"}
            
    raise HTTPException(status_code=404, detail="NOT FOUND ")





 