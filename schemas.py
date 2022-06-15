#from this import s
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional
import random
from dateutil.relativedelta import relativedelta

class TaxCodeFormatError(Exception):
    ''' Custom error that is raised when a tax code doesn't have the right format'''
    
    def __init__(self, value: str, message: str)-> None:
        self.value = value
        self.message = message
        super().__init__(message)



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
            raise TaxCodeFormatError(value=val, message="Tax code should contain numbers only.")
        if len(val)!= 8:
            raise TaxCodeFormatError(value=val,message="Tax code should be 8 digits long")
        return val

class Customers(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    dob: datetime
    phone: str
    password: str
    created_on: datetime
    
class Passwords(BaseModel):
    pwd_id = int
    customer_id = int
    pwd = str
    active = bool
    created_on = datetime


    
