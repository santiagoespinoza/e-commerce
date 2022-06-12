import json
from tkinter import N
import pandas as pd
from datetime import datetime
from schemas import Products, Users, Categories

with open("./Data/Hikvision_products.json", encoding="utf8") as data_file:
    data = json.load(data_file)

products = []
for i in range(len(data)):
    for j in range(len(data[i]['productos'])):
        dct = data[0]['productos'][j]
        p = Products(product_id = dct['producto_id'], description=dct['descripcion'], sku = dct['total_existencia'],
                    suggested_price = dct['precios']['precio_1'], partner_price = dct['precios']['precio_especial'],
                    current_stock = dct['existencia']['nuevo'], stock_lastupdate = datetime.utcnow(), tax_code = dct['sat_key'],
                    tax_unit_code = dct['unidad_de_medida']['clave_unidad_sat'], wv_ratio = dct['pvol'], weight = dct['peso'],
                    length = dct['largo'], width = dct['ancho'], height = dct['alto'], brit_unit = dct['unidad_de_medida']['codigo_unidad'],
                    cat1 = dct['categorias'][2]['nombre'], cat2 = dct['categorias'][1]['nombre'], cat3 = dct['categorias'][0]['nombre'])
        products.append(p)

with open("./Data/ecommerce_users.json", encoding="utf8") as data_file:
    user_data = json.load(data_file)

users = []
for i in range(len(user_data)):
    dct = user_data[i]
    u = Users(id = dct['id'], first_name = dct['first_name'], last_name = dct['last_name'], 
            email = dct['email'], user_name = dct['user_name'], password = dct['password'],
            hashed_password = dct['hashed_password'], street = dct['street'], city = dct['city'], 
            state = dct['state'], postal_code = dct['postal_code'], billing_address=dct['billing_address'],
            shipping_address=dct['shipping_address'], card_num1=dct['card_number_1'], card_num2=dct['card_number_2'], 
            card_num3=dct['card_number_3'])
    users.append(u)


with open("./Data/Categories.json", encoding = "utf8") as data_file:
    cat_data = json.load(data_file)

categories = []
for i in range(len(cat_data['subcategorias'])):
    dct = cat_data['subcategorias'][0]
    c = Categories(id=dct['id'], name=dct['nombre'], level=dct['nivel'])
    categories.append(c)
