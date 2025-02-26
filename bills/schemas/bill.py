from pydantic import BaseModel, Field
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
    bill_type: BillType
    amount: float = Field(gt=0)
    date: date
    description: Optional[str] = None
    paid: bool = False
    user_id: int
