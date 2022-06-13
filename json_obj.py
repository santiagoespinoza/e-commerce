import json
from datetime import datetime
from schemas import Products, Customers, Categories
from database import SessionLocal
import models as mo
import random

with open("./Data/Hikvision_products.json", encoding="utf8") as data_file:
    data = json.load(data_file)

products = []
for i in range(len(data)):
    for j in range(len(data[i]['productos'])):
        dct = data[i]['productos'][j]
        p = Products(product_id = dct['producto_id'], description=dct['descripcion'], sku = dct['total_existencia'],
                    suggested_price = dct['precios']['precio_1'], partner_price = dct['precios']['precio_especial'],
                    current_stock = dct['existencia']['nuevo'], stock_lastupdate = datetime.utcnow(), tax_code = dct['sat_key'],
                    tax_unit_code = dct['unidad_de_medida']['clave_unidad_sat'], wv_ratio = dct['pvol'], weight = dct['peso'],
                    length = dct['largo'], width = dct['ancho'], height = dct['alto'], brit_unit = dct['unidad_de_medida']['codigo_unidad'],
                    cat1 = dct['categorias'][2]['nombre'], cat2 = dct['categorias'][1]['nombre'], cat3 = dct['categorias'][0]['nombre'])
        products.append(p)

print(len(products))

session = SessionLocal()
session.query(mo.Products).delete()

# We fill products table
for i in range(len(products)):
    row = products[i]

    tmp = mo.Products(
        product_id = row.product_id,
        description = row.description,
        sku = row.sku,
        suggested_price = row.suggested_price,
        partner_price = row.partner_price,
        current_stock = row.current_stock,
        stock_lastupdate = row.stock_lastupdate,
        tax_code = row.tax_code,
        tax_unit_code = row.tax_unit_code,
        wv_ratio = row.wv_ratio,
        weight = row.weight,
        length = row.length,
        width = row.width,
        height = row.height,
        brit_unit = row.brit_unit,
        cat1 = row.cat1,
        cat2 = row.cat2,
        cat3 = row.cat3
    )
    session.add(tmp)
    session.commit()

with open("./Data/ecommerce_users.json", encoding="utf8") as data_file:
    user_data = json.load(data_file)

for i in range(len(user_data)):
    dct = user_data[i]
    phone_num = ''.join([str(random.randint(1, 10)) for _ in range(9)])
    u = mo.Customers(
        customer_id=dct['id'], first_name = dct['first_name'], last_name = dct['last_name'], dob=random.randrange(18, 80),
            email = dct['email'], user_name = dct['user_name'], pwd = dct['password'], created_on=datetime.utcnow(),phone = phone_num)
    session.add(u)
    session.commit()


with open("./Data/Categories.json", encoding = "utf8") as data_file:
    cat_data = json.load(data_file)

categories = []
for i in range(len(cat_data['subcategorias'])):
    dct = cat_data['subcategorias'][0]
    c = Categories(id=dct['id'], name=dct['nombre'], level=dct['nivel'])
    categories.append(c)

