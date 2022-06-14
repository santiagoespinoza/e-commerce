#from this import s
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import random
from dateutil.relativedelta import relativedelta

class Users(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    user_name: str
    password: str
    hashed_password: str
    street: str
    city: str
    state: str
    postal_code: str
    billing_address: bool
    shipping_address: bool
    card_num1: str
    card_num2: Optional[str]=None
    card_num3: Optional[str]=None


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
    cat1: str
    cat2: str
    cat3: str

class Passwords(BaseModel):
    pwd_id = int
    customer_id = int
    pwd = str
    active = bool
    created_on = datetime

class Customers(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    #phone: int = Field(default_factory=(random.randint(1, 10) for _ in range(9)))
    #dob: datetime = Field(default_factory = datetime.utcnow() - relativedelta(years=random.randrange(18,80),months = random.randrange(1,12),days = random.randrange(0,365)))
    password: str
    #created_on: datetime = Field(default_factory = datetime.utcnow())
    
