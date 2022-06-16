from database import Base, engine, SessionLocal
import models 

print("Creating database ....")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

