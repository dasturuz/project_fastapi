from sqlalchemy import Column, Integer, String, Boolean,Float,Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from db import Base

class Orders(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now, nullable=False)
    status = Column(Boolean, nullable=False, default=True)