from psycopg2 import IntegrityError
from pydantic import BaseModel
import json
from database import SessionLocal
from typing import List, Optional
from schemas import Customers, Products
import models as mo
from datetime import datetime

session = SessionLocal() # We start a session
# We delete table data
session.query(mo.Customers).delete()
session.query(mo.Products).delete()

# Loading customer data and creating pydantic instances
with open("./Data/ecommerce_users.json", encoding="utf8") as data_file:
    data = json.load(data_file)
    customers: List[Customers] = [Customers(**item) for item in data]

# upoading customer data to the sql database
for i in range(len(customers)):
    row_cust = customers[i]
    tmp_cust = mo.Customers(**dict(row_cust))
    session.add(tmp_cust)
    session.commit()

# Creating pydantic model with product data
products = []
with open("./Data/Hikvision_products.json",encoding="utf8") as prod_file:
    prod_data = json.load(prod_file)
    for i in range(len(prod_data)):
        for j in range(len(prod_data[i]['productos'])):
            dct = prod_data[i]['productos'][j]
            p = Products(
                product_id = dct['producto_id'], 
                description=dct['descripcion'], 
                sku = dct['total_existencia'],
                suggested_price = dct['precios']['precio_1'],
                partner_price = dct['precios']['precio_especial'],
                current_stock = dct['existencia']['nuevo'],
                stock_lastupdate = datetime.utcnow(),
                tax_code = dct['sat_key'],
                tax_unit_code = dct['unidad_de_medida']['clave_unidad_sat'],
                wv_ratio = dct['pvol'],
                weight = dct['peso'],
                length = dct['largo'], 
                width = dct['ancho'],
                height = dct['alto'],
                brit_unit = dct['unidad_de_medida']['codigo_unidad'],
                cat1 = dct['categorias'][2]['nombre'],
                cat2 = dct['categorias'][1]['nombre'],
                cat3 = dct['categorias'][0]['nombre']
            )
            products.append(p)

# uploading data to the sql database
for i in range(len(products)):
    row = products[i]
    try:
        tmp = mo.Products(**dict(row))
        session.add(tmp)
    except IntegrityError as e:
        pass
    finally:
        session.commit()





