from database.app.orders_operations import *
from utils.validation import validate_order_details
from database.app.orders_operations import add_order
from utils.enums import Status


def accept_order(customer_id, product_id, quantity):
    validate_order_details(customer_id, product_id, quantity)
    add_order(customer_id, product_id, quantity, status = Status.APPROVED);



# Store order details customerID, productID, quantity, statys
# Update order status?
