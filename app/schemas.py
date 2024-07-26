from datetime import datetime
from pydantic import BaseModel,EmailStr
from typing import Optional
from pydantic.types import conint

# class Post(BaseModel):
#   title:str
#   content:str
#   published : bool=True
#   # rating: Optional[int]=None

class PostBase(BaseModel):
  title:str
  content:str
  published : bool=True

  class Config:
    orm_mode=True
    from_attributes=True
  

class PostCreate(PostBase):
  pass

class userOut(BaseModel):
  id: int
  email: EmailStr
  created_at: datetime
  
class Post(PostBase):
  id:int
  created_at: datetime
  owner_id: int
  owner: userOut

class PostOut(PostBase):
  post: Post
  votes: int

class UserCreate(BaseModel):
  email: EmailStr
  password: str


class UserLogin(BaseModel):
  email: EmailStr
  password: str

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  id: Optional[str]=None


class Vote(BaseModel):
  post_id: int
  dir: conint(le=1)
