from sqlalchemy import Column, Integer, String, Boolean,Float,Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from db import Base

class Customers(Base):
    __tablename__ = "Customers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    phone_number = Column(Integer, nullable=False)
    location = Column(String(50), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now, nullable=False)
    status = Column(Boolean, nullable=False, default=True)