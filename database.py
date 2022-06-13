from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import json_obj as jo

engine = create_engine("postgresql://postgres:masha@localhost/e-commerce", echo = True)

Base = declarative_base()

SessionLocal = sessionmaker(bind = engine)

# We fill products table
for i in range(len(jo.products)):
    row = jo.products[i]