import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from utils.enums import Status

load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@localhost:5432/{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(100))


class Warehouse(Base):
    __tablename__ = "warehouses"

    warehouse_id = Column(Integer, primary_key=True, autoincrement=True)
    warehouse_address = Column(String(255), nullable=False)
    warehouse_name = Column(String(255))


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(255), nullable=False)
    customer_address = Column(String(255), nullable=False)


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(Enum(Status), nullable=False)


class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    warehouse_id = Column(Integer, ForeignKey("warehouses.warehouse_id"), nullable=False)
    quantity = Column(Integer, nullable=False)


def get_session():
    """Return a new database session."""
    return SessionLocal()


def execute_query(query: str):
    """Execute a raw SQL query string."""
    try:
        with engine.begin() as conn: 
            conn.execute(text(query))
        print("Query executed successfully.")
    except SQLAlchemyError as e:
        print(f"Database error: {e}")


def create_tables():
    """Create all tables defined in the ORM models."""
    try:
        Base.metadata.create_all(engine)
        print("Tables created successfully.")
    except SQLAlchemyError as e:
        print(f"Error creating tables: {e}")
