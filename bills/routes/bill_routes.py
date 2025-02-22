from fastapi import APIRouter, HTTPException, Depends, status
from typing import Annotated
from pymysql import IntegrityError
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import BillBase, BillType

router = APIRouter(
    prefix="/bills",
    tags=["bills"]
)

db_dependency = Annotated[Session, Depends(get_db)]

# Create a Bill
@router.post("", response_model=str, status_code=status.HTTP_201_CREATED)
async def create_bill(bill: BillBase, db: db_dependency):
    try:
        user = db.query(models.User).filter(models.User.id == bill.user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail=f"User with id {bill.user_id} not found")

        db_bill = models.Bill(**bill.model_dump())
        db.add(db_bill)
        db.commit()
        db.refresh(db_bill) 
        return "Bill created successfully"
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Bill already exists") 
    
# Get all Bills
@router.get("", response_model=list[BillBase], status_code=status.HTTP_200_OK)
async def get_bills(db: db_dependency):
    try:
        bills = db.query(models.Bill).all()
        if not bills:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bills not found")
        return bills
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#Get Bills by Bill Type    
@router.get("/type/{bill_type}", response_model=list[BillBase], status_code=status.HTTP_200_OK)
async def get_bills_by_type(bill_type: BillType, db: db_dependency):
    try:
        bills = db.query(models.Bill).filter(models.Bill.bill_type == bill_type).all()
        if not bills:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bills not found")
        return bills
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))
    
# Get a Bill by ID
@router.get("/{bill_id}", response_model=BillBase, status_code=status.HTTP_200_OK)
async def get_bill(bill_id: int, db: db_dependency):
    try:
        bill_result = db.query(models.Bill).filter(models.Bill.id == bill_id).first()
        if bill_result is not None:
            return bill_result
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bill not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Update a Bill
@router.put("/{bill_id}", response_model=BillBase, status_code=status.HTTP_200_OK)
async def update_bill(bill_id: int, bill: BillBase, db: db_dependency):
    try:
        bill_result = db.query(models.Bill).filter(models.Bill.id == bill_id).first()
        if bill_result is not None:
            bill_result.update(bill.model_dump())
            db.commit()
            return bill_result
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bill not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Get Bills by User ID
@router.get("/user/{user_id}", response_model=list[BillBase], status_code=status.HTTP_200_OK)
async def get_bills_by_user(user_id: int, db: db_dependency):
    try:
        bills = db.query(models.Bill).filter(models.Bill.user_id == user_id).all()
        if not bills:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bills not found")
        return bills
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Update Bills paid status
@router.put("/{bill_id}/paid", response_model=BillBase, status_code=status.HTTP_200_OK)
async def update_bill_paid(bill_id: int, paid: bool, db: db_dependency):
    try:
        bill_result = db.query(models.Bill).filter(models.Bill.id == bill_id).first()
        if bill_result is not None:
            bill_result.paid = paid
            db.commit()
            return bill_result
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bill not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Delete a Bill
@router.delete("/{bill_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bill(bill_id: int, db: db_dependency):
    try:
        bill_result = db.query(models.Bill).filter(models.Bill.id == bill_id).first()
        if bill_result is not None:
            db.delete(bill_result)
            db.commit()
            return
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bill not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))