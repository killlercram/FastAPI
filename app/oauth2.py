from jose import JWTError,jwt
from datetime import datetime,timedelta,timezone
from . import schemas
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
#SECRET_KEY
#Algorithm
#Expiration time

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY="b0dbac97a1f47232fbaa2ff013fbe8cbdc199fb724093fef8b94541b24f2c3fc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
 to_encode= data.copy()

 expire=datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
 to_encode.update({"expiration":expire.isoformat()})

 encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

 return encoded_jwt


def verify_access_token(token: str, credentials_exception):
 
  try:
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])

    id: str=payload.get("user_id")

    if id is None:
      raise credentials_exception
    token_data=schemas.TokenData(id=str(id))

  except JWTError:
    raise credentials_exception
  return token_data
  
def get_current_user(token: str = Depends(oauth2_scheme)):
  credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})

  return verify_access_token(token,credentials_exception)








