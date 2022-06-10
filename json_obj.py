import json
import pandas as pd
from datetime import datetime
from schemas import Categories, Products

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
                    length = dct['largo'], width = dct['ancho'], height = dct['alto'], brit_unit = dct['unidad_de_medida']['codigo_unidad'])
        products.append(p)

print(len(products))