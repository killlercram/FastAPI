from fastapi import FastAPI
from .database import engine
from . import models 
from .routers import post,user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)


app=FastAPI()


origins = [
    "http://google.com",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
app.include_router(vote.router)

@app.get("/")
async def root():
  return {"message":"Hello World"}
  

 