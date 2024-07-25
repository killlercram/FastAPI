from fastapi import FastAPI
from .database import engine
from . import models 
from .routers import post,user,auth
from .config import settings

print(settings.database_name)
models.Base.metadata.create_all(bind=engine)


app=FastAPI()


# my_posts=[{"title" :"title of post 1","content":"content of post 1","id":1},{"title" :"title of post 2","content":"content of post 2","id":2}]

# #function to get the details for the particular id
# def postById(id):
#   for p in my_posts:
#     if p["id"]==id:
#       return p
    
# #function for finding index
# def find_index_post(id):
#   for i,p in enumerate (my_posts):
#     if p["id"]==id:
#       return i
    

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
  return {"message":"Hello World"}
  

 