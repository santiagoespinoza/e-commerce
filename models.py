from email.policy import default
from operator import length_hint
from typing import Collection

from pandas import describe_option
from database import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

class Passwords(Base):
    __tablename__ = 'passwords'
    pwd_id = Column(Integer, primary_key = True)
    customer_id = Column(Integer)
    pwd = Column(String(256))
    active = Column(Boolean)
    created_on = Column(DateTime)

    #customers = relationship('Customers', backref = 'passwords')

class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    #dob = Column(DateTime)
    #phone = Column(String)
    password = Column(String)

    #password = relationship('Passwords', backref = 'customers')

class Products(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key = True)
    description = Column(String)
    sku = Column(String)
    suggested_price = Column(Float)
    partner_price = Column(Float)
    current_stock = Column(Integer)
    stock_lastupdate = Column(DateTime)
    tax_code = Column(String)
    tax_unit_code = Column(String)
    wv_ratio = Column(String)
    weight = Column(String)
    length = Column(String)
    width = Column(String)
    height = Column(String)
    brit_unit = Column(Boolean)
    cat1 = Column(String)
    cat2 = Column(String)
    cat3 = Column(String)