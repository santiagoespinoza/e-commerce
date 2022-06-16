from urllib.request import Request
from django.http import JsonResponse
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from database import SessionLocal
import models
import schemas as sc
from val import customers, products
from sqlalchemy import and_ 

app = FastAPI()
db = SessionLocal()

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc, ValueError):
    return JSONResponse(
        content={"message":str(exc)}
    )

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

# Create item and upload it to the database
@app.post('/Products/', status_code=200)
def create_product(prod:sc.Products):
    try:
        new_prod = models.Products(**dict(prod))
        db.add(new_prod)
        db.commit()
    except sc.TaxCodeFormatError as e:
        raise HTTPException(status_code=400, detail = e.message)
    return prod

# Register new user
@app.post('/Users/Register')
def register_user(user:sc.Customers):
    # Check if email is being used already
    if (any(customers[i].email==user.email for i in range(len(customers)))):
        raise HTTPException(status_code=400, detail = 'Email already in use')
    new_user = models.Customers(**dict(user))

    customers.append(user)
    db.add(new_user)
    db.commit()

    return user

