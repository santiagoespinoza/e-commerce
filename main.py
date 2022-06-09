from fastapi import FastAPI
from schemas import Password, Customers
from database import SessionLocal

app = FastAPI()

db = SessionLocal()