from db import execute_query

def add_inventory(product_id, warehouse_id, quantity):
    execute_query("""INSERT INTO inventory ({product_id}, {warehouse_id}, {quantity});""")

def get_product(product_id, warehouse_id):
    execute_query("""SELECT * FROM inventory WHERE product_id = {product_id} AND warehouse_id = {warehouse_id};""")


def update_inventory(product_id, warehouse_id, new_quantity):
    execute_query("""UPDATE inventory SET quantity = {new_quantity} WHERE product_id = {prodcut_id} AND warehouse_id = {warehouse_id} ;""")

def delete_inventory():
    execute_query("""DELETE FROM inventory WHERE product_id = {prodcut_id} AND warehouse_id = {warehouse_id} ;""")