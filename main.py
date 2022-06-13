from typing import List
from typing import List
from fastapi import FastAPI, status
from numpy import product
from database import SessionLocal
from json_obj import products, users, categories
import models
import schemas as sc

app = FastAPI()
db = SessionLocal()

@app.get('/')
def root():
    return users



@app.get('/products', response_model=List[sc.Products], status_code=200)
def get_product():
    prod = db.query(models.Products).all()
    return prod


@app.post('/item', status_code=status.HTTP_201_CREATED)
def create(p:sc.Passwords):
    new_p = models.Passwords(
        pwd_id = p.pwd_id,
        customer_id = p.customer_id,
        pwd = p.pwd,
        active = -p.active,
        created_on = p.created_on 
    )

    db.add(new_p)
    db.commit()

    return new_p