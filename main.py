from urllib.request import Request
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from database import SessionLocal
import models
import schemas as sc
from sqlalchemy import and_
from sqlalchemy.orm.exc import UnmappedInstanceError

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
@app.post('/Products/', status_code=201)
def create_product(prod:sc.Products):
    # Check if product id is already used in the database
    id_exists = bool(db.query(models.Products).filter(models.Products.product_id==prod.product_id).first())
    if id_exists:
        raise HTTPException(status_code=400, detail = 'Product ID is not unique')

    new_prod = models.Products(**dict(prod))
    db.add(new_prod)
    db.commit()
    return prod

# Delete a product from its ID
@app.delete('/Products/Delete{prod_id}')
def delete_product(prod_id:int):
    try:
        # We query the item we want deleted
        prod_del = db.query(models.Products).filter(models.Products.product_id==prod_id).first()

        # we delete the item and commit
        db.delete(prod_del)
        db.commit()
    except UnmappedInstanceError:
        raise HTTPException(status_code=404, detail="Product not Found")

    return prod_del

# Update a Products\
@app.patch('/Products/{id}')
def update_product(id:int, prod: sc.Products):
    prod_up = db.query(models.Products).filter(models.Products.product_id==id).first()

    prod_up.description = prod.description
    prod_up.sku = prod.sku
    prod_up.suggested_price = prod.suggested_price
    prod_up.partner_price = prod.partner_price
    prod_up.current_stock = prod.current_stock
    prod_up.tax_code = prod.tax_code
    prod_up.tax_unit_code = prod.tax_unit_code
    prod_up.wv_ratio = prod.wv_ratio
    prod_up.weight = prod.weight
    prod_up.length = prod.length
    prod_up.width = prod.width
    prod_up.height = prod.height
    prod_up.brit_unit = prod.brit_unit
    prod_up.cat1 = prod.cat1
    prod_up.cat2 = prod.cat2
    prod_up.cat3 = prod.cat3

    db.commit()
    return prod_up


# Register new user
@app.post('/Users/Register', status_code=201)
def register_user(user:sc.Customers):
    # Check if the users id or email is already in the database
    email_exists = bool(db.query(models.Customers).filter(models.Customers.email == user.email))
    id_exists = bool(db.query(models.Customers).filter(models.Customers.id==0).first())
    # If the user the email or id are not in use we create a new user
    if not email_exists or not id_exists:
        new_user = models.Customers(**dict(user))
        #ucustomers.append(user)
        db.add(new_user)
        db.commit()
    else:
        raise HTTPException(status_code=400, detail='Customer already exists')

    return user

# Delete a user from its ID
@app.delete('/Users/Delete{user_id}')
def delete_user(user_id:int):
    try:
        user_del = db.query(models.Customers).filter(models.Customers.id==user_id).first()
        db.delete(user_del)
        db.commit()
    except UnmappedInstanceError:
        raise HTTPException(status_code=404, detail="User not found")

    return user_del

# Update User information
@app.put('/Users/Update{user_id}',status_code=200)
def update_user(user_id:int, user: sc.Customers):
    user_up = db.query(models.Customers).filter(models.Customers.id==user_id).first()

    user_up.first_name = user.first_name
    user_up.last_name = user.last_name
    user_up.email = user.email
    user_up.dob = user.dob
    user_up.phone = user.phone
    user_up.password = user.password

    db.commit()
    return user_up



