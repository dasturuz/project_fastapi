from pydantic import BaseModel
from pydantic.datetime_parse import datetime

class ProductTypeBase(BaseModel):
    name: str
    date: datetime
    status: bool

class CreateProductType(BaseModel):
    name: str

class UpdateProductType(ProductTypeBase):
    id:int

class DeleteProductType(ProductTypeBase):
    id:int