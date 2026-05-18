from utils.validation import validate_order_details
from database.app.orders_operations import add_order, get_order


def accept_order(customer_id: int, product_id: int, quantity: int):
    validate_order_details(customer_id, product_id, quantity)
    add_order(customer_id, product_id, quantity)


def order_exists(order_id:int) -> bool:
    return get_order(order_id) != None
