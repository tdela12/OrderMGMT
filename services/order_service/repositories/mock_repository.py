from app.model import OrderModel
from app.schema import Order
from typing import List, Optional


class MockOrderRepository:
    def __init__(self, warehouses: list):
        self.warehouses = warehouses

    def add(self, order: Order) -> Optional[Order]:
        try:
            order_db = OrderModel(**order.model_dump())
            self.session.add(order_db)
            self.session.commit()
            self.session.refresh(order_db)
            return Order.model_validate(order_db)
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error adding order: {e}")
            return None

    def get_by_id(self, order_id: int) -> Optional[Order]:
        try:
            order_db = self.session.query(OrderModel).get(order_id)
            if not order_db:
                print(f"No order found with ID: {order_id}")
                return None
            return Order.model_validate(order_db)
        except SQLAlchemyError as e:
            print(f"Error fetching order: {e}")
            return None

    def list_all(self) -> List[Order]:
        try:
            orders_db = self.session.query(OrderModel).all()
            return [Order.model_validate(o) for o in orders_db]
        except SQLAlchemyError as e:
            print(f"Error listing orders: {e}")
            return []

    def update(self, order: Order) -> Optional[Order]:
        try:
            order_db = self.session.query(OrderModel).get(order.order_id)
            if not order_db:
                print(f"No order found with ID: {order.order_id}")
                return None
            order_db.product_id = order.product_id
            order_db.quantity = order.quantity
            order_db.status = order.status
            self.session.commit()
            self.session.refresh(order_db)
            return Order.model_validate(order_db)
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error updating order: {e}")
            return None

    def delete(self, order_id: int) -> bool:
        try:
            order_db = self.session.query(OrderModel).get(order_id)
            if not order_db:
                print(f"No order found with ID: {order_id}")
                return False
            self.session.delete(order_db)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error deleting order: {e}")
            return False