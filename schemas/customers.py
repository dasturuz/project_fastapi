from pydantic import BaseModel
from pydantic.datetime_parse import datetime

class CustomersBase(BaseModel):
    name: str
    date: datetime
    location: str
    phone_number:int
    status: bool

class CreateCustomer(BaseModel):
    name: str
    location: str
    phone_number:int

class UpdateCustomer(BaseModel):
    id: int
    name: str
    date: datetime
    location: str
    phone_number: int

class DeleteCustomer(CustomersBase):
    id:int