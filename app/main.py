from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app=FastAPI()

class Post(BaseModel):
  title:str
  content:str
  published : bool=True
  rating: Optional[int]=None

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
    
@app.get("/")
async def root():
  return {"message":"Hello World"}

@app.get("/posts")
def get_posts():
  return {"data": my_posts}

#inserting the data inside
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
 post_dict=post.dict()
 post_dict['id']=randrange(3,1000000)
 my_posts.append(post_dict)
 return{"data":post_dict}

#retreving single post
@app.get("/posts/{id}") 
def get_post(id:int,response: Response):
  post=postById(id)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id: {id} was not found")
  return {"Post_details": post} 

#Deleting the post
@app.delete("/deletes/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
  # find the index in the database then remove it
  # my_posts.pop(index)
  index =find_index_post(id)
  if index==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} does not exist")
  my_posts.pop(index)

  #updation
@app.put("/posts/{id}")
def update_post(id:int,post:Post):
     index =find_index_post(id)
     if index==None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} does not exist")
     
     post_dict=post.dict()
     post_dict['id']=id
     my_posts[index]=post_dict
     return{"data":post_dict}
  

  

