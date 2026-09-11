from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql+psycopg://postgres:Postgre%40Manya@localhost:5432/Sanskritee_db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind = engine)

try:
    with engine.connect() as connection:
        print("Database connected successfully")
except Exception as e:
    print("Database connection failed!")
    print(e)