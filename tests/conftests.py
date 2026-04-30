import pytest
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def conn():
    connection = psycopg2.connect(
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        host="localhost",
        password=os.getenv("POSTGRES_PASSWORD"),
        port=5432,
    )
    yield connection
    connection.close()

@pytest.fixture(autouse=True)
def rollback_after_test(conn):
    yield
    conn.rollback()