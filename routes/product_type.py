from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)


from functions.product_types import *
from schemas.product_types import *

router_productType = APIRouter()



@router_productType.post('/add',)
def add_product_type(form: CreateProductType, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) : #
    if product_type_add(form, db) :
        raise HTTPException(status_code = 200, detail = "Amaliyot muvaffaqiyatli amalga oshirildi")


@router_productType.get('/',  status_code = 200)
def get_product_types(search: str = None, status: bool = True, id: int = 0,roll : str = None, page: int = 1, limit: int = 25, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) : # current_user: User = Depends(get_current_active_user)
    if id :
        return one_product_type(id, db)
    else :
        return all_product_types(search, status, page, limit, db)


@router_productType.put("/update")
def product_type_update(form: UpdateProductType, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)) :
    if update_product_type(form, db) :
        raise HTTPException(status_code = 200, detail = "Amaliyot muvaffaqiyatli amalga oshirildi")

@router_productType.delete('/{id}',  status_code = 200)
def product_type_delete(id: int = 0,db: Session = Depends(get_db), current_user: UserCurrent = Depends(get_current_active_user)) : # current_user: User = Depends(get_current_active_user)
    if id :
        return delete_product_type(id, db)