from typing import List
from typing import List
from fastapi import FastAPI, status
from numpy import product
from database import SessionLocal
import models
from sqlalchemy import and_

app = FastAPI()
db = SessionLocal()

@app.get('/', status_code=200)
def get_product():
    prod = db.query(models.Products).all()
    return prod

# Get items by their category
@app.get('/Products/{cat}', status_code=200)
def get_cat(cat:str):
    prod = db.query(models.Products).filter(models.Products.cat3==cat).all()
    return prod

# Get item by its id
@app.get('/Products/{cat}/{id}', status_code=200)
def get_cat(cat:str, id: int):
    prod = db.query(models.Products).filter(and_(models.Products.cat3==cat, models.Products.product_id == id)).all()
    return prod