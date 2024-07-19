
from .. import models,schemas,utils,oauth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from ..database import SessionLocal, engine,get_db
from sqlalchemy.orm import Session
from typing import Optional,List

router=APIRouter(
  prefix="/posts",
  tags=['Posts']
)

@router.get("/",response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db),user_id: int =Depends(oauth2.get_current_user)):
  # cursor.execute("""Select * from posts""")
  # posts=cursor.fetchall()
  posts=db.query(models.Post).all()
  return  posts



#creating the data inside
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post: schemas.PostCreate,db: Session = Depends(get_db),user_id: int =Depends(oauth2.get_current_user)):
  
  # cursor.execute("""insert into posts (title,content,published) values (%s,%s,%s) returning * """,(post.title,post.content,post.published))
  # new_post=cursor.fetchone()
  # conn.commit()

  new_post=models.Post(**post.model_dump())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return  new_post



#retreving single post
@router.get("/{id}",response_model=schemas.Post) 
def get_post(id:int,response: Response,db: Session = Depends(get_db),user_id: int =Depends(oauth2.get_current_user)):
  # print(test_post)
  # post=postById(id)

  # cursor.execute("""select * from posts where id= %s """,(str(id)))
  # post=cursor.fetchone()

  post=db.query(models.Post).filter(models.Post.id==id).first()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id: {id} was not found")
  return  post


#Deleting the post
@router.delete("/deletes/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),user_id: int =Depends(oauth2.get_current_user)):
  # find the index in the database then remove it
  # my_posts.pop(index)
  # index =find_index_post(id)

  # cursor.execute("""delete from posts where id= %s  returning * """,(str(id)))
  # deleted_post =cursor.fetchone()
  # conn.commit()

  deleted_post=db.query(models.Post).filter(models.Post.id==id)

  if deleted_post.first()==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} does not exist")
  deleted_post.delete(synchronize_session=False)
  db.commit()
  # my_posts.pop(index)


  #updation
@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,post:schemas.PostCreate,db: Session = Depends(get_db),user_id: int =Depends(oauth2.get_current_user)):
  #  index =find_index_post(id)

  # cursor.execute("""update posts set title = %s ,content = %s ,published= %s where id = %s returning *""" ,(post.title,post.content,post.published,str(id)))
  # updated_post=cursor.fetchone()
  # conn.commit()

  post_query=db.query(models.Post).filter(models.Post.id==id)
  updated_post=post_query.first()

  if updated_post==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} does not exist")
    #  post_dict=post.dict()
    #  post_dict['id']=id
    #  my_posts[index]=post_dict
  post_query.update(post.model_dump(),synchronize_session=False)
  db.commit()
  post_query.first()