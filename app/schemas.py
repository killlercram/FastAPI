from datetime import datetime
from pydantic import BaseModel

# class Post(BaseModel):
#   title:str
#   content:str
#   published : bool=True
#   # rating: Optional[int]=None

class PostBase(BaseModel):
  title:str
  content:str
  published : bool=True

class PostCreate(PostBase):
  pass

class Post(BaseModel):
  id:int
  title: str
  content: str
  published: bool
  created_at: datetime