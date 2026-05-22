from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from model import InventoryModel
from schema import Inventory
from typing import List, Optional


class InventoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, inventory: Inventory) -> Optional[Inventory]:
        try:
            inventory_db = InventoryModel(**inventory.model_dump())
            self.session.add(inventory_db)
            self.session.commit()
            self.session.refresh(inventory_db)
            return Inventory.model_validate(inventory_db)
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error adding inventory: {e}")
            return None

    def get_by_product_and_warehouse(self, product_id: int, warehouse_id: int) -> Optional[Inventory]:
        try:
            inventory_db = (
                self.session.query(InventoryModel)
                .filter_by(product_id=product_id, warehouse_id=warehouse_id)
                .first()
            )
            if not inventory_db:
                print(f"No inventory found for product {product_id} in warehouse {warehouse_id}")
                return None
            return Inventory.model_validate(inventory_db)
        except SQLAlchemyError as e:
            print(f"Error fetching inventory: {e}")
            return None

    def list_all(self) -> List[Inventory]:
        try:
            inventory_db = self.session.query(InventoryModel).all()
            return [Inventory.model_validate(i) for i in inventory_db]
        except SQLAlchemyError as e:
            print(f"Error listing inventory: {e}")
            return []

    def update(self, inventory: Inventory) -> Optional[Inventory]:
        try:
            inventory_db = (
                self.session.query(InventoryModel)
                .filter_by(product_id=inventory.product_id, warehouse_id=inventory.warehouse_id)
                .first()
            )
            if not inventory_db:
                print(f"No inventory found for product {inventory.product_id} in warehouse {inventory.warehouse_id}")
                return None
            inventory_db.quantity = inventory.quantity
            self.session.commit()
            self.session.refresh(inventory_db)
            return Inventory.model_validate(inventory_db)
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error updating inventory: {e}")
            return None

    def delete(self, product_id: int, warehouse_id: int) -> bool:
        try:
            inventory_db = (
                self.session.query(InventoryModel)
                .filter_by(product_id=product_id, warehouse_id=warehouse_id)
                .first()
            )
            if not inventory_db:
                print(f"No inventory found for product {product_id} in warehouse {warehouse_id}")
                return False
            self.session.delete(inventory_db)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error deleting inventory: {e}")
            return False