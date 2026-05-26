from repository import InventoryRepository
from schema import Inventory

class InventoryService:
     def __init__(self, repository: InventoryRepository):
          self.repository = repository
          
     def available_to_sell(self, product_id: int, warehouse_id:int) -> Inventory | None:
          inventory = self.repository.get_by_product_and_warehouse(product_id, warehouse_id)
          return inventory.quantity > 0