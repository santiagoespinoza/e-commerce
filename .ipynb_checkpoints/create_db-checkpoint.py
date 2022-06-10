from database import Base, engine
from models import Customers, Passwords

print("Creating database ....")

Base.metadata.create_all(engine)