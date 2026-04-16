from sqlalchemy import create_engine
from models import Base

# 1. This tells SQLAlchemy where to create the database file
# 'sqlite:///warehouse.db' creates a file named warehouse.db in this folder
engine = create_engine('sqlite:///warehouse.db')

# 2. This looks at all the classes in models.py and creates matching tables
# It uses the attributes like client_name and sku to set up the columns
Base.metadata.create_all(engine)

print("Warehouse database has been created successfully!")