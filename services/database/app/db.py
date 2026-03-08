import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import OperationalError, errorcodes, errors
import sys

load_dotenv()

conn = psycopg2.connect(
    database = os.getenv("POSTGRES_DB"),
    user = os.getenv("POSTGRES_USER"),
    host = "localhost",
    password = os.getenv("POSTGRES_PASSWORD"),
    port = 5432,
)

def print_psycopg2_exception(err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    # get the line number when exception occured
    line_num = traceback.tb_lineno

    # print the connect() error
    print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
    print ("psycopg2 traceback:", traceback, "-- type:", err_type)

    # psycopg2 extensions.Diagnostics object attribute
    print ("\nextensions.Diagnostics:", err.diag)

    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()

    except psycopg2.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()
    
    print("Query executed successfully.")

def create_tables():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS products(
        product_id SERIAL PRIMARY KEY, 
        product_name VARCHAR(100));
        """,
        """
        CREATE TABLE IF NOT EXISTS warehouses(
        warehouse_id SERIAL PRIMARY KEY,
        warehouse_address VARCHAR(255) NOT NULL, 
        warehouse_name VARCHAR(255));
        """,
        """
        CREATE TABLE IF NOT EXISTS customers(
        customer_id SERIAL PRIMARY KEY,
        customer_name VARCHAR(255) NOT NULL,
        customer_address VARCHAR(255) NOT NULL);
        """,
        """
        CREATE TABLE IF NOT EXISTS orders(
        order_id SERIAL PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        status VARCHAR(255) NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id));
        """,
        """
        CREATE TABLE IF NOT EXISTS inventory(
        inventory_id SERIAL PRIMARY KEY,
        product_id INTEGER NOT NULL,
        warehouse_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id));
        """
    ]
    try:
        with conn.cursor() as cur:
            for command in commands:
                cur.execute(command)
        conn.commit()

    except psycopg2.DatabaseError as e:
        print_psycopg2_exception(e)

        conn.rollback()