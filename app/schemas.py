from datetime import datetime
from pydantic import BaseModel,EmailStr
from typing import Optional

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

class Post(PostBase):
  id:int
  created_at: datetime


class UserCreate(BaseModel):
  email: EmailStr
  password: str

class userOut(BaseModel):
  id: int
  email: EmailStr
  created_at: datetime

class UserLogin(BaseModel):
  email: EmailStr
  password: str

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  id: Optional[str]=None