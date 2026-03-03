from db import execute_query

## Define crud operations 

def add_warehouse(warehouse_address, warehouse_name = None):
    execute_query(""" INSERT INTO warehouses ({warehouse_name}, {warehouse_address});""")


def get_warehouse_by_id(warehouse_id):
    execute_query(""" SELECT * FROM warehouses WHERE warehouse_id = {warehouse_id};""")

def update_warehouse(warehouse_id, new_warehouse_address, new_warehouse_name = None):
    execute_query("""UPDATE warehouses SET warehouse_address = {new_warehouse_address}, warehouse_name = {new_warehouse_name} WHERE warehouse_id = {warehouse_id} ;""")

def delete_warehouse():
    execute_query("""DELETE FROM warehouses WHERE warehouse_id = {warehouse_id} ;""")