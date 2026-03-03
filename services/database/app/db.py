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

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()

    except psycopg2.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

    finally:
        if conn:
            conn.close()

