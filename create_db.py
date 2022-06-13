from database import Base, engine, SessionLocal
import models as mo

print("Creating database ....")

Base.metadata.create_all(engine)
