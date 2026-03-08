from db import execute_query, conn


## Define crud operations 
def add_warehouse(warehouse_address, warehouse_name = None):
    execute_query(f""" INSERT INTO warehouses (warehouse_name, warehouse_address) VALUES ('{warehouse_name}', '{warehouse_address}');""")

def get_warehouse(warehouse_id):
    #Get warehouse by id
    execute_query(f""" SELECT * FROM warehouses WHERE warehouse_id = '{warehouse_id}';""")

def update_warehouse(warehouse_id, new_warehouse_address = None, new_warehouse_name = None):
    if new_warehouse_address != None:
        execute_query(f"""UPDATE warehouses SET warehouse_address = '{new_warehouse_address}' WHERE warehouse_id = '{warehouse_id}' ;""")
    if new_warehouse_name != None:
        execute_query(f"""UPDATE warehouses SET warehouse_name = '{new_warehouse_name}' WHERE warehouse_id = '{warehouse_id}' ;""")

def delete_warehouse(warehouse_id):
    execute_query(f"""DELETE FROM warehouses WHERE warehouse_id = '{warehouse_id}' ;""")

add_warehouse("123 Main St", "Warehouse A")
add_warehouse("456 Elm St", "Warehouse B")
get_warehouse(1)
update_warehouse(1, new_warehouse_address = "789 Oak St")
delete_warehouse(2)
