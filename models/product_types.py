from sqlalchemy import Column, Integer, String, Boolean,Float,Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from db import Base

class Product_types(Base):
    __tablename__ = "Product_types"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(20), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now, nullable=False)
    status = Column(Boolean, nullable=False, default=True)