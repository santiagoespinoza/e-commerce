from database import SessionLocal
from val import customers, products, passwords, payment, addresses
import models as mo

session = SessionLocal() # We start a session
# We delete table data
session.query(mo.Customers).delete()
session.query(mo.Products).delete()
session.query(mo.Passwords).delete()
session.query(mo.Addresses).delete()
session.query(mo.Payment).delete()

# uploading customer data to the sql database
for i in range(len(customers)):
    row_cust = customers[i]
    tmp_cust = mo.Customers(**dict(row_cust))
    session.add(tmp_cust)

# uploading data to the sql database
for i in range(len(products)):
    row = products[i]
    tmp = mo.Products(**dict(row))
    session.add(tmp)

for i in range(len(passwords)):
    dct = {"pwd_id":passwords[i].pwd_id, "pwd":passwords[i].pwd}
    tmp_pass = mo.Passwords(**dct)
    session.add(tmp_pass)

for i in range(len(addresses)):
    dct = {"id":addresses[i].id,"street":addresses[i].street, "street_num":addresses[i].street_num, "city":addresses[i].city, 
    "state":addresses[i].state, "postal_code":addresses[i].postal_code, "billing_address":addresses[i].billing_address,"shipping_address":addresses[i].shipping_address}
    tmp_add = mo.Addresses(**dct)
    session.add(tmp_add)

for i in range(len(payment)):
    dct = {"id":payment[i].id, "card_num":payment[i].card_num, "current":True}
    tmp_pay = mo.Payment(**dct)
    session.add(tmp_pay)
     
session.commit() 


    