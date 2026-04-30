from utils.validation import validate_order_details
from database.app.orders_operations import add_order


def accept_order(customer_id: int, product_id: int, quantity: int):
    validate_order_details(customer_id, product_id, quantity)
    add_order(customer_id, product_id, quantity)


# Store order details customerID, productID, quantity, statys
# Update order status?
