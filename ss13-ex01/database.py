from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#Định nghĩa host database bao gồm host, username, password 
DATABASE_URL = "mysql+pymysql://naul:Nq4wPX)}-^t9V2?@malis-database.mysql.database.azure.com:3306/fastapi"

#Tạo kết nối tới database
engine = create_engine(url=DATABASE_URL, pool_size=10)
#Khởi tạo phiên làm việc
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
#Lấy phiên làm việc ra gán cho biến db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#Tạo 1 lớp để bọc các model dùng trong sqlalchemy
class Base(DeclarativeBase):
    pass

