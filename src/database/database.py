from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 
from pydantic import PostgresDsn

SQLALCHEMY_DATABASE_URI = PostgresDsn.build(
    scheme="postgresql",
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_SERVER"),
    path=f"/{os.getenv('DATABASE_DB')}",
)


engine = create_engine(
    SQLALCHEMY_DATABASE_URI
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
