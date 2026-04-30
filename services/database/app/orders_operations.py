from sqlalchemy.exc import SQLAlchemyError
from db import get_session, Order
from utils.enums import Status


def add_order(customer_id: int, product_id: int, quantity: int):
    """Create a new order."""
    session = get_session()
    try:
        order = Order(customer_id=customer_id, product_id=product_id, quantity=quantity, status=Status.APPROVED)
        session.add(order)
        session.commit()
        session.refresh(order)
        print(f"Order created with ID: {order.order_id}")
        return order
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error creating order: {e}")
    finally:
        session.close()


def get_order(order_id: int):
    """Fetch an order by ID."""
    session = get_session()
    try:
        order = session.get(Order, order_id)
        if not order:
            print(f"No order found with ID: {order_id}")
        return order
    except SQLAlchemyError as e:
        print(f"Error fetching order: {e}")
    finally:
        session.close()


def update_order_status(order_id: int, new_status: Status):
    """Update the status of an order."""
    session = get_session()
    try:
        order = session.get(Order, order_id)
        if not order:
            print(f"No order found with ID: {order_id}")
            return None
        order.status = new_status
        session.commit()
        session.refresh(order)
        return order
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error updating order status: {e}")
    finally:
        session.close()


def delete_order(order_id: int):
    """Delete an order by ID."""
    session = get_session()
    try:
        order = session.get(Order, order_id)
        if not order:
            print(f"No order found with ID: {order_id}")
            return False
        session.delete(order)
        session.commit()
        print(f"Order {order_id} deleted.")
        return True
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error deleting order: {e}")
    finally:
        session.close()
