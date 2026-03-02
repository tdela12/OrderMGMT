import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    database = f"{os.getenv("POSTGRES_DB")}",
    user = f"{os.getenv("POSTGRES_USER")}",
    host = "localhost",
    password = f"{os.getenv("POSTGRES_PASSWORD")}",
    port = 5432,
)

def add_product():
    commands = ("""
        INSERT INTO products 
        """
       )
    try:
        with conn.cursor() as cur:
            for command in commands:
                cur.execute(command)
        conn.commit()

    except psycopg2.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

    finally:
        if conn:
            conn.close()
