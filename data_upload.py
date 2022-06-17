import psycopg2
from psycopg2.errors import UniqueViolation
from database import SessionLocal
from val import customers, products
import models as mo

session = SessionLocal() # We start a session
# We delete table data
session.query(mo.Customers).delete()
session.query(mo.Products).delete()

# upoading customer data to the sql database
for i in range(len(customers)):
    row_cust = customers[i]
    tmp_cust = mo.Customers(**dict(row_cust))
    session.add(tmp_cust)

# uploading data to the sql database
for i in range(len(products)):
    row = products[i]
    tmp = mo.Products(**dict(row))
    session.add(tmp)
    session.commit()

    