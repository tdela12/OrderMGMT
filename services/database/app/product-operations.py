from db import execute_query

def add_product(product):
    execute_query(""" INSERT INTO products ({product});""")


def get_product_by_name(product_name = None):
    execute_query(""" SELECT * FROM products WHERE product_name = {product_name}; """)

def update_product_name(product_name, new_product_name):
    execute_query(""" UPDATE products SET product_name = {new_product_name} WHERE product_name = {product_name}; """)

def delete_product(product_name):
    execute_query(""" DELETE FROM products WHERE product_name = {product_name}; """)
