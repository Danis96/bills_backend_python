from sqlalchemy import Column, DateTime, Enum, Integer, String, Float, Boolean, ForeignKey
from database import Base
from schemas import BillType
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Bill(Base):
    __tablename__ = "bills"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    bill_type: Mapped[str] = mapped_column(String(50)) 
    amount: Mapped[float] = mapped_column(Float)
    date: Mapped[datetime] = mapped_column(DateTime)
    description: Mapped[str] = mapped_column(String(255))
    paid: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=50), unique=True)
    email = Column(String(length=100), unique=True)