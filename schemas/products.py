from pydantic import BaseModel
from pydantic.datetime_parse import datetime

class ProductBase(BaseModel):
    name: str
    new_price: int
    old_price: int
    comment: str
    status: bool
    date: datetime
    product_type: str

class CreateProduct(BaseModel):
    name: str
    new_price: int
    old_price: int
    comment: str
    product_type: str
    status: bool

class UpdateProduct(ProductBase):
    id:int

class DeleteProduct(ProductBase):
    id:int