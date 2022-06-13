from database import Base, engine, SessionLocal
import models as mo
import json_obj as jo

print("Creating database ....")

Base.metadata.create_all(engine)

# We fill products table
for i in range(len(jo.products)):
    row = jo.products[i]

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

    session = SessionLocal()
    session.add(tmp)
    session.commit()