from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from menu_service import get_all, create_menu, detail_menu, update_menu, delete_menu
from database import get_db
from schemas import MenuRequest

app = FastAPI()

#Khởi tạo router cho lấy toàn bộ ds menu
@app.get("/menu-items")
def get_all_menus(request: Request, db: Session = Depends(get_db)):
    return get_all(request, db)

#Khởi tạo router cho thêm menu
@app.post("/menu-items")
def add_menu(request: Request, menu: MenuRequest, db: Session = Depends(get_db)):
    #Gọi service create_menu và trả về json luôn
    return create_menu(request, db, menu)

#Khởi tạo router cho lấy chi tiết 1 menu
@app.get("/menu-items/{item_id}")
def get_detail_menu(request: Request, item_id: int, db: Session = Depends(get_db)):
    #//
    return detail_menu(request, db, item_id)

#Khởi tạo router cho cập nhật menu
@app.put("/menu-items/{item_id}")
def update_menus(request: Request, item_id: int, menu_update: MenuRequest, db: Session = Depends(get_db)):
    #//
    return update_menu(request, db, item_id, menu_update)

#Khởi tạo router cho xóa 1 menu
@app.delete("/menu-items/{item_id}")
def update_menus(request: Request, item_id: int, db: Session = Depends(get_db)):
    #//
    return delete_menu(request, db, item_id)