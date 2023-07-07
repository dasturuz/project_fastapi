from sqlalchemy import Column, Integer, String, Boolean,Float,Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from db import Base

class Products(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(20), nullable=False)
    product_type = Column(String(50), nullable=False)
    old_price = Column(Integer, nullable=False)
    new_price = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    date = Column(DateTime(timezone=True), default=func.now, nullable=False)
    status = Column(Boolean, nullable=False, default=True)