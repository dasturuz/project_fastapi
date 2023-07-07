from fastapi import Depends
from sqlalchemy.orm import Session
from models.products import Products
from db import Base, get_db
from schemas.products import *
from utils.pagination import pagination
import datetime


def all_products(search, status, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Products.name.like(search_formatted)
    else:
        search_filter = Products.id > 0
    if status in [True, False]:
        status_filter = Products.status == status
    else:
        status_filter = Products.id > 0

    product = db.query(Products).filter(search_filter, status_filter)
    if page and limit:
        return pagination(product, page, limit)
    else:
        return product.all()


def one_product(id, db):
    return db.query(Products).filter(Products.id == id).first()


def product_add(form, db):
    new_product = Products(
        name = form.name,
        new_price = form.new_price,
        old_price = form.old_price,
        comment = form.comment,
        product_type = form.product_type,
        date = datetime.datetime.min,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"data": "Muvaffaqiyatli qo'shildi"}


def read_product(db):
    products = db.query(Products).all()
    return products


def update_product(form, db):
    product = db.query(Products).filter(Products.id == form.id).update({
        Products.id: form.id,
        Products.date: form.date,
        Products.new_price: form.new_price,
        Products.old_price: form.old_price,
        Products.comment: form.comment,
        Products.status: form.status,
        Products.product_type: form.product_type,
        Products.status: form.status
    })
    db.commit()
    return {"Malumot yangilandi"}


def delete_product(id: int, db):
    product = db.query(Products).filter(Products.id == id).update({
        Products.status: False
    })
    db.commit()
    return {"Malumot o'chirildi"}
