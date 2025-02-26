from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    # email: EmailStr
    
    # class Config:
    #     from_attributes = True

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int 

class Token(BaseModel):
    access_token: str
    token_type: str