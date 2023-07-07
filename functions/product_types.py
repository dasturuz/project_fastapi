from fastapi import Depends
from sqlalchemy.orm import Session
from models.product_types import Product_types
from db import Base, get_db
from schemas.product_types import *
from utils.pagination import pagination
import datetime


def all_product_types(search, status, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Product_types.name.like(search_formatted)
    else:
        search_filter = Product_types.id > 0
    if status in [True, False]:
        status_filter = Product_types.status == status
    else:
        status_filter = Product_types.id > 0

    productType = db.query(Product_types).filter(search_filter, status_filter)
    if page and limit:
        return pagination(productType, page, limit)
    else:
        return productType.all()


def one_product_type(id, db):
    return db.query(Product_types).filter(Product_types.id == id).first()


def product_type_add(form, db):
    new_product_type = Product_types(
        name = form.name,
        date = datetime.datetime.min,
    )
    db.add(new_product_type)
    db.commit()
    db.refresh(new_product_type)
    return {"data": "Muvaffaqiyatli qo'shildi"}


def read_product_type(db):
    users = db.query(Product_types).all()
    return users


def update_product_type(form, db):
    user = db.query(Product_types).filter(Product_types.id == form.id).update({
        Product_types.id: form.id,
        Product_types.name: form.name,
        Product_types.date: form.date,
        Product_types.status: form.status
    })
    db.commit()
    return {"Malumot yangilandi"}


def delete_product_type(id: int, db):
    order = db.query(Product_types).filter(Product_types.id == id).update({
        Product_types.status: False
    })
    db.commit()
    return {"Malumot o'chirildi"}
