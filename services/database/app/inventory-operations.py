from db import execute_query

def add_inventory(product_id, warehouse_id, quantity):
    execute_query(f"""INSERT INTO inventory (product_id, warehouse_id, quantity) VALUES ('{product_id}', '{warehouse_id}', '{quantity}');""")

def get_product(product_id, warehouse_id):
    execute_query(f"""SELECT * FROM inventory WHERE product_id = '{product_id}' AND warehouse_id = '{warehouse_id}';""")


def update_inventory(product_id, warehouse_id, new_quantity):
    execute_query(f"""UPDATE inventory SET quantity = '{new_quantity}' WHERE product_id = '{product_id}' AND warehouse_id = '{warehouse_id}' ;""")

def delete_inventory(product_id, warehouse_id):
    execute_query(f"""DELETE FROM inventory WHERE product_id = '{product_id}' AND warehouse_id = '{warehouse_id}' ;""")

add_inventory(1, 1, 100)
add_inventory(2, 1, 50)
get_product(1, 1)
update_inventory(1, 1, 150)
delete_inventory(1, 1)