from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app=FastAPI()

class Post(BaseModel):
  title:str
  content:str
  published : bool=True
  # rating: Optional[int]=None

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
    
@app.get("/")
async def root():
  return {"message":"Hello World"}

@app.get("/posts")
def get_posts():
  cursor.execute("""Select * from posts""")
  posts=cursor.fetchall()
  # print(posts)
  return {"data": posts}

#inserting the data inside
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
#  post_dict=post.dict()
#  post_dict['id']=randrange(3,1000000)
#  my_posts.append(post_dict)
#  return{"data":post_dict}
  cursor.execute("""insert into posts (title,content,published) values (%s,%s,%s) returning * """,(post.title,post.content,post.published))
  new_post=cursor.fetchone()
  conn.commit()
  return {"data": new_post}

#retreving single post
@app.get("/posts/{id}") 
def get_post(id:int,response: Response):
  cursor.execute("""select * from posts where id= %s """,(str(id)))
  post=cursor.fetchone()
  # print(test_post)
  # post=postById(id)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id: {id} was not found")
  return {"Post_details": post} 

#Deleting the post
@app.delete("/deletes/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
  # find the index in the database then remove it
  # my_posts.pop(index)
  # index =find_index_post(id)
  cursor.execute("""delete from posts where id= %s  returning * """,(str(id)))
  deleted_post =cursor.fetchone()
  conn.commit()

  if deleted_post==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} does not exist")
  # my_posts.pop(index)

  #updation
@app.put("/posts/{id}")
def update_post(id:int,post:Post):
  cursor.execute("""update posts set title = %s ,content = %s ,published= %s where id = %s returning *""" ,(post.title,post.content,post.published,str(id)))
  updated_post=cursor.fetchone()
  conn.commit()
  #  index =find_index_post(id)
  if updated_post==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} does not exist")
    #  post_dict=post.dict()
    #  post_dict['id']=id
    #  my_posts[index]=post_dict
  return{"data": updated_post}
  

  

