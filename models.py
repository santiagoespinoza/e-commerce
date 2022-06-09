from email.policy import default
from typing import Collection
from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

class Passwords(Base):
    __tablename__ = 'passwords'
    pwd_id = Column(Integer, primary_key = True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    pwd = Column(String(256))
    active = Column(Boolean)
    created_on = Column(DateTime)

    customers = relationship('Customers', backref = 'passwords')

class Customers(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    dob = Column(DateTime)
    phone = Column(String)
    pwd = Column(String, ForeignKey('passwords.pwd'))

    password = relationship('Passwords', backref = 'customers')

