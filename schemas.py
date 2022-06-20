from pydantic import BaseModel, validator, Field
from typing import Optional
from datetime import datetime

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

    @validator("tax_code")
    @classmethod
    def valid_tax_code(cls, val):
        '''Validator to check if tax code is valid.'''

        chars = [c for c in val if c in "0123456789"]
        if val.isdecimal() != True:
            raise ValueError("Tax code should contain numbers only.")
        if len(val)!= 8:
            raise ValueError("Tax code should be 8 digits long")
        return val

class Customers(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str = Field(unique=True)
    dob: datetime
    phone: str
    created_on: datetime
    
class Passwords(BaseModel):
    pwd_id: int
    pwd: str
    active: bool
    created_on: datetime

class Addresses(BaseModel):
    id: int
    street: str
    street_num: str
    street_ext: Optional[str]=None
    city: str
    state: str
    postal_code: str
    billing_address: bool
    shipping_address: bool

class Payment(BaseModel):
    id: int
    card_num: str
    current: bool

    @validator("card_num")
    @classmethod
    def validate_card_num(cls, val):
        ''' Validator to check if card number is valid'''
        chars = [c for c in val if c in "0123456789"]

        if val.isdecimal() != True:
            raise ValueError("Card number should contain numbers only.")
        if len(val)!=16:
            raise ValueError("Card Number should be 16 digits long")
        return val
        


    
