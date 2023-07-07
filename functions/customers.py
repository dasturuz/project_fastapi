from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from models.customers import Customers
from db import Base, get_db
from schemas.users import *
from utils.pagination import pagination
import datetime

def all_customers(search, status, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Customers.name.like(search_formatted) | Customers.phone_number.like(search_formatted)
    else:
        search_filter = Customers.id > 0
    if status in [True, False]:
        status_filter = Customers.status == status
    else:
        status_filter = Customers.id > 0

    basket = db.query(Customers).filter(search_filter, status_filter)
    if page and limit:
        return pagination(basket, page, limit)
    else:
        return basket.all()


def one_customer(id, db):
    return db.query(Customers).filter(Customers.id == id).first()


def customer_add(form, db):
    new_customer = Customers(
        name = form.name,
        phone_number = form.phone_number,
        location = form.location,
        date = datetime.datetime.min,
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return {"data": "Muvaffaqiyatli qo'shildi"}


def read_customer(db):
    users = db.query(Customers).all()
    return users


def update_customer(form, db):
    if one_customer(form.id, db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli foydalanuvchi mavjud emas")
    user_verification = db.query(Customers).filter(Customers.name == form.name).first()
    if user_verification and user_verification.id != form.id:
        raise HTTPException(status_code=400, detail="Bunday foydalanuvchi mavjud")

    customer = db.query(Customers).filter(Customers.id == form.id).update({
        Customers.id: form.id,
        Customers.name: form.name,
        Customers.date: datetime.datetime.min,
        Customers.location: form.location,
        Customers.phone_number: form.phone_number
    })
    db.commit()
    return {"Malumot yangilandi"}


def delete_customer(id: int, db):
    if one_customer(id, db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli customer mavjud emas")
    order = db.query(Customers).filter(Customers.id == id).update({
        Customers.status: False
    })
    db.commit()
    return {"Malumot o'chirildi"}
