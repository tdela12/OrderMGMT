from utils.validation import validate_order_details
from database.app.orders_operations import add_order, get_order
from inventory_service.app.inventory_service import available_to_sell
from repository import OrderRepository
from schema import Order


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def get_order(self, order_id: int) -> Order | None:
        return self.repository.get_by_id(order_id)
    
    def add_order(self, order: Order) -> Order | None:
        return self.repository.add(order)

    def order_exists(self, order_id:int) -> bool:
        return self.repository.get_by_id != None

