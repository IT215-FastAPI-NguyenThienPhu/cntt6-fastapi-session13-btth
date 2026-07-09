from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/pet_db"

engine = create_engine(url=DATABASE_URL, pool_size=10)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
class Base(DeclarativeBase):
    pass