from db import execute_query

def add_order(customer_id, product_id, quantity, status):
    execute_query(f"""INSERT INTO orders (customer_id, product_id, quantity, status) VALUES ('{customer_id}', '{product_id}', '{quantity}', '{status}');""")

def get_order(order_id):
    execute_query(f"""SELECT * FROM orders WHERE order_id = '{order_id}';""")

def update_order_status(order_id, new_status):
    execute_query(f"""UPDATE orders SET status = '{new_status}' WHERE order_id = '{order_id}';""")

def delete_order(order_id):
    execute_query(f"""DELETE FROM orders WHERE order_id = '{order_id}';""")

add_order(1, 1, 10, "pending")
add_order(2, 2, 5, "pending")
get_order(1)
update_order_status(1, "shipped")
delete_order(1)