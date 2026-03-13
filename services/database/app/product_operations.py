from db import execute_query

def add_product(product):
    execute_query(f""" INSERT INTO products (product_name) VALUES ('{product}');""")

def get_product(product_name):
    #Get product by name
    execute_query(f""" SELECT * FROM products WHERE product_name = '{product_name}'; """)

def update_product(product_name, new_product_name):
    execute_query(f""" UPDATE products SET product_name = '{new_product_name}' WHERE product_name = '{product_name}'; """)

def delete_product(product_name):
    execute_query(f""" DELETE FROM products WHERE product_name = '{product_name}'; """)

add_product("Product A")
add_product("Product B")

get_product("Product A")

update_product("Product A", "Product C")
delete_product("Product B")
