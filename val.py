import json
import random
import re
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
            created_on = datetime.utcnow()
        )
        customers.append(u)


# Creating pydantic model with product data
products = []
unique = []
with open("./Data/Hikvision_products.json",encoding="utf8") as prod_file:
    prod_data = json.load(prod_file)

    # We remove duplicate entries
    for i in prod_data:
        if i not in unique:
            unique.append(i)

for i in range(len(unique)):
    for j in range(len(unique[i]['productos'])):
        dct = unique[i]['productos'][j]
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

passwords = []
for i in range(len(data)):
    user = data[i]
    pwrd = sc.Passwords(
        pwd_id = i,
        pwd = user['password'],
        active = True,
        created_on = datetime.utcnow()
    )
    passwords.append(pwrd)

addresses = []
for i in range(len(data)):
    user = data[i]
    add = sc.Addresses(
        id = i,
        street = re.split(r'(?<=\d)(?:-\d+)?\s+',user['street'])[1],
        street_num = re.split(r'(?<=\d)(?:-\d+)?\s+',user['street'])[0],
        street_ext = re.split(r'(?<=\d)(?:-\d+)?\s+',user['street'])[1],
        city = user['city'],
        state = user['state'],
        postal_code = user['postal_code'],
        billing_address = user['billing_address'],
        shipping_address = user['shipping_address']
    )
    addresses.append(add)

print([addresses[i].street for i in range(len(addresses))])

payment = []
for i in range(len(data)):
    user = data[i]
    pay = sc.Payment(
        id = i, 
        card_num = user['card_number_1'],
        current = True,
        created_on = datetime.utcnow() 
    )
    payment.append(pay)