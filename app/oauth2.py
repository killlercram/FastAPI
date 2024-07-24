from jose import JWTError,jwt
from datetime import datetime,timedelta,timezone
from . import schemas,database,models
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
#SECRET_KEY
#Algorithm
#Expiration time

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY="G4YkPn8K/Ik5KjQyZWI5YXk1dPZhS0s0Qk9UM0lMdzg="
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
 to_encode= data.copy()

 expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
 to_encode.update({"expiration":expire.isoformat()})

 encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

 return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = str(payload.get("user_id"))
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data
  
def get_current_user(token: str = Depends(oauth2_scheme),db: Session =Depends(database.get_db)):
  credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})

  token=verify_access_token(token,credentials_exception)

  user=db.query(models.User).filter(models.User.id == token.id).first()
  if user is None:
    raise credentials_exception

  return user








