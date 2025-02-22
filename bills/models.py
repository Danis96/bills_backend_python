from sqlalchemy import Column, DateTime, Integer, String, Float, Boolean, ForeignKey
from database import Base
from datetime import datetime


class Bill(Base):
    __tablename__ = "bills"

    id: Column[int] = Column(Integer, primary_key=True)
    bill_type: Column[str] = Column(String(50)) 
    amount: Column[float] = Column(Float)
    date: Column[datetime] = Column(DateTime)
    description: Column[str] = Column(String(255))
    paid: Column[bool] = Column(Boolean, default=False)
    user_id: Column[int] = Column(ForeignKey("users.id"))



class User(Base):
    __tablename__ = "users"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    username: Column[str] = Column(String(length=50), unique=True)
    email: Column[str] = Column(String(length=100), unique=True)