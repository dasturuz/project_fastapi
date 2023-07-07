from pydantic import BaseModel
from pydantic.datetime_parse import datetime

class OrdersBase(BaseModel):
    name: str
    date: datetime
    status: bool

class CreateOrder(BaseModel):
    name: str

class UpdateOrder(OrdersBase):
    id:int

class DeleteOrder(OrdersBase):
    id:int