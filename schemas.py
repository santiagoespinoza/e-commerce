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

class Categories(BaseModel):
    id: int
    name:str
    level:str

class Products(BaseModel):
    product_id: int
    description: str
    sku: str
    suggested_price: float
    partner_price: float
    current_stock: int
    stock_lastupdate: datetime
    tax_code: str
    tax_unit_code: str
    wv_ratio: str
    weight: str
    length: str
    width: str
    height: str
    brit_unit: bool
    