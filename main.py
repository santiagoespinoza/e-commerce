from fastapi import FastAPI
from numpy import product
from database import SessionLocal
from json_obj import products, users, categories

app = FastAPI()


@app.get('/')
def root():
    return users

db = SessionLocal()