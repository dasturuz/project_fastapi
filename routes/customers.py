from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)


from functions.customers import *
from schemas.customers import *

router_customer = APIRouter()



@router_customer.post('/add',)
def add_customer(form: CreateCustomer, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) : #
    if customer_add(form, db) :
        raise HTTPException(status_code = 200, detail = "Amaliyot muvaffaqiyatli amalga oshirildi")


@router_customer.get('/',  status_code = 200)
def get_customers(search: str = None, status: bool = True, id: int = 0,roll : str = None, page: int = 1, limit: int = 25, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) : # current_user: User = Depends(get_current_active_user)
    if id :
        return one_customer(id, db)
    else :
        return all_customers(search, status, page, limit, db)


@router_customer.put("/update")
def customer_update(form: UpdateCustomer, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)) :
    if update_customer(form, db):
        raise HTTPException(status_code = 200, detail = "Amaliyot muvaffaqiyatli amalga oshirildi")

@router_customer.delete('/{id}',  status_code = 200)
def customer_delete(id: int = 0,db: Session = Depends(get_db), current_user: UserCurrent = Depends(get_current_active_user)) : # current_user: User = Depends(get_current_active_user)
    if id :
        return delete_customer(id, db)