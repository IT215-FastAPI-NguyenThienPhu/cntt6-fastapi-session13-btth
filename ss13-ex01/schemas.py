from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import Any
from datetime import datetime, timezone

#Đinh nghĩa những trường chỉ cho phép dùng Enum 
class Status(str, Enum):
    AVAILABLE = "AVAILABLE"
    OUT_OF_STOCK = "OUT_OF_STOCK"

#Khai báo dữ liệu gửi lên 
class MenuRequest(BaseModel):
    dish_code: str
    dish_name: str
    calorie_count: int
    price: float
    status: Status

#Khai báo dữ liệu trả về
class MenuResponse(BaseModel):
    id: int
    dish_code: str
    dish_name: str
    calorie_count: int
    price: float
    status: str

    #Định nghĩa là cho phép kiểu sqlalchemy chuyển sang kiểu pydantic
    model_config = ConfigDict(from_attributes=True)

#Cấu trúc trả về cho toàn api
class StandardResponse(BaseModel):
    statusCode: int
    data: Any | None =None
    error: Any | None =None
    message: str
    path: str
    timestamp: str

#Chuyển lớp StandardResponse về dạng JSONResponse
def standard_response(status_code: int, data: Any,error: Any, message: str, path: str):
    #Gán giá trị cho StandardReponse và chuyển về dạng dir 
    content_response = StandardResponse(
        statusCode=status_code,
        data=data,
        error=error,
        message=message,
        path=path,
        timestamp=datetime.now(timezone.utc).isoformat()
    ).model_dump()

    return JSONResponse(
        status_code=status_code,
        content=content_response
    )
