import json
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta
import schemas as sc

# Loading customer data and creating pydantic instances
customers = []
with open("./Data/ecommerce_users.json", encoding="utf8") as data_file:
    data = json.load(data_file)
    for i in range(len(data)):
        user = data[i]
        date_of_birth = datetime.utcnow() - relativedelta(years=random.randrange(18,80),months = random.randrange(1,12),days = random.randrange(0,365))
        u = sc.Customers(
            id = user['id'],
            first_name = user['first_name'],
            last_name = user['last_name'],
            email = user['email'],
            dob = date_of_birth,
            phone = ''.join([str(random.randint(1, 9)) for _ in range(10)]),
            password= user['password'],
            created_on = datetime.utcnow()
        )
        customers.append(u)


# Creating pydantic model with product data
products = []
with open("./Data/Hikvision_products.json",encoding="utf8") as prod_file:
    prod_data = json.load(prod_file)
    for i in range(len(prod_data)):
        for j in range(len(prod_data[i]['productos'])):
            dct = prod_data[i]['productos'][j]
            p = sc.Products(
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
