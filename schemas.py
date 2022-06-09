from pydantic import BaseModel
from datetime import datetime

class Password(BaseModel):
    pwd_id: int
    customer_id: int
    pwd: str
    active: bool
    created_on: datetime

    class Config:
        orm_mode = True

class Customers(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    dob: datetime
    phone: str
    pwd: str
    created_on: datetime

    class Config:
        orm_mode = True

    
    