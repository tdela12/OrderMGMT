from inventory_service.app.inventory_service import available_to_sell
from services.order_service.repositories.repository import OrderRepository
from schema import Order
from utils.enums import Status
from typing import List


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository
        
    def get_order_status(self, order_id: int) -> Status | None:
        return self.repository.get_by_id(order_id).status

    def get_order(self, order_id: int) -> Order | None:
        return self.repository.get_by_id(order_id)
    
    def add_order(self, order: Order) -> Order | None:
        return self.repository.add(order)

    def order_exists(self, order_id:int) -> bool:
        return self.repository.get_by_id != None
    
    def list_all_orders(self) -> List[Order]:
        return self.repository.list_all()

