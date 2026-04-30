import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from services.api_gateway.app import main  # adjust to your actual import path

import os

from services.database.app.db import Base, Customer, Product, Warehouse, Order, Inventory

@pytest.fixture
def client():
    return TestClient(main)

load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@localhost:5432/{os.getenv('POSTGRES_DB')}"
)


@pytest.fixture(scope="session")
def engine():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture
def session(engine):
    """Each test gets a session that is rolled back on teardown."""
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    session.close()
    transaction.rollback()
    connection.close()


# --- Reusable seed fixtures ---

@pytest.fixture
def sample_customer(session):
    customer = Customer(customer_name="Alice Smith", customer_address="123 Main St")
    session.add(customer)
    session.flush()  # assigns customer_id without committing
    return customer


@pytest.fixture
def sample_product(session):
    product = Product(product_name="Widget")
    session.add(product)
    session.flush()
    return product


@pytest.fixture
def sample_warehouse(session):
    warehouse = Warehouse(warehouse_name="Warehouse A", warehouse_address="456 Industrial Rd")
    session.add(warehouse)
    session.flush()
    return warehouse


@pytest.fixture
def sample_order(session, sample_customer, sample_product):
    order = Order(
        customer_id=sample_customer.customer_id,
        product_id=sample_product.product_id,
        quantity=3,
        status="pending"
    )
    session.add(order)
    session.flush()
    return order


@pytest.fixture
def sample_inventory(session, sample_product, sample_warehouse):
    inventory = Inventory(
        product_id=sample_product.product_id,
        warehouse_id=sample_warehouse.warehouse_id,
        quantity=100
    )
    session.add(inventory)
    session.flush()
    return inventory