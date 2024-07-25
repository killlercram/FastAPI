# This will handle the database connection
import time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor
from .config import settings

# SQLALCHEMY_DATABASE_URL='postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'

SQLALCHEMY_DATABASE_URL=f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"


engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#as we are using this to connect to our database we are directly using sqlAlchemy and not using this

# while True:
#   try:
#     conn=psycopg2.connect(host='localhost',database='Fastapi',user='postgres',password='pass@121',cursor_factory=RealDictCursor)
#     cursor=conn.cursor()
#     print("Database connection was successfull!!")
#     break
#   except Exception as error:
#     print("Connecting to database failed")
#     print("Error: ",error)
#     time.sleep(2)