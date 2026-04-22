from db import execute_query

def add_customer(customer_id, customer_name, customer_address):
    execute_query(f""" INSERT INTO customers (customer_id, customer_name, customer_address) VALUES ('{customer_id}, {customer_name}, {customer_address}');""")

def get_customer(customer_id):
    #Get product by name
    execute_query(f""" SELECT * FROM products WHERE customer_id = '{customer_id}'; """)

def update_product(customer_id, new_product_name):
    execute_query(f""" UPDATE products SET product_name = '{customer_id}' WHERE product_name = '{product_name}'; """)

def delete_product(customer_id):
    execute_query(f""" DELETE FROM products WHERE customer_id = '{customer_id}'; """)
