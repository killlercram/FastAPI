from typing import List
from fastapi import FastAPI,Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .database import SessionLocal, engine,get_db
from sqlalchemy.orm import Session
from . import models 
from .routers import post,user,auth

models.Base.metadata.create_all(bind=engine)


app=FastAPI()



while True:
  try:
    conn=psycopg2.connect(host='localhost',database='Fastapi',user='postgres',password='pass@121',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print("Database connection was successfull!!")
    break
  except Exception as error:
    print("Connecting to database failed")
    print("Error: ",error)
    time.sleep(2)


my_posts=[{"title" :"title of post 1","content":"content of post 1","id":1},{"title" :"title of post 2","content":"content of post 2","id":2}]

#function to get the details for the particular id
def postById(id):
  for p in my_posts:
    if p["id"]==id:
      return p
    
#function for finding index
def find_index_post(id):
  for i,p in enumerate (my_posts):
    if p["id"]==id:
      return i
    

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
  return {"message":"Hello World"}
  

 