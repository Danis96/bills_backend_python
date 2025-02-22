from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import date

class BillType(str, Enum):
    ELECTRICITY = "ELEKTROPRIVREDA"
    HEATING = "TOPLANE_PLIN"
    WATER = "VODOVOD"
    UTILITIES = "KOMUNALNE_USLUGE"
    BUILDING_MAINTENANCE = "ODRZAVANJE_ZGRADE"

class BillBase(BaseModel):
    id: int
    bill_type: BillType
    amount: float
    date: date
    description: Optional[str] = None
    paid: Optional[bool] = False
    user_id: int

class UserBase(BaseModel):
    id: int
    username: str
    email: str