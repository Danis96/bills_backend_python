from fastapi import APIRouter, HTTPException, Depends, status
from typing import Annotated
from pymysql import IntegrityError
from sqlalchemy.orm import Session

from schemas.user import UserBase, UserRead
from database import get_db
from models import User
from routes.auth_routes import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[User, Depends(get_current_user)]


# Get all Users
@router.get("", response_model=list[UserRead], status_code=status.HTTP_200_OK)
async def get_users(db: db_dependency):
    try:
        users = db.query(User).all()
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#Get current logged in user
@router.get("/me", response_model=UserRead)
async def get_logged_in_user(user: user_dependency):
    return user    

# Get a User by ID
@router.get("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: db_dependency):
    try:
        user_result = db.query(User).filter(User.id == user_id).first()
        if user_result is not None:
            return user_result
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found") 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Delete a User
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: db_dependency):
    try:
        user_result = db.query(User).filter(User.id == user_id).first()
        if user_result is not None:
            db.delete(user_result)
            db.commit()
            return
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
