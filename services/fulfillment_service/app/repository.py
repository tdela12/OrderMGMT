from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from model import WarehouseModel
from schema import Warehouse
from typing import List, Optional


class WarehouseRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, warehouse: Warehouse) -> Optional[Warehouse]:
        try:
            warehouse_db = WarehouseModel(**warehouse.model_dump())
            self.session.add(warehouse_db)
            self.session.commit()
            self.session.refresh(warehouse_db)
            return Warehouse.model_validate(warehouse_db)
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error adding warehouse: {e}")
            return None

    def get_by_id(self, warehouse_id: int) -> Optional[Warehouse]:
        try:
            warehouse_db = self.session.get(WarehouseModel, warehouse_id)
            if not warehouse_db:
                print(f"No warehouse found with ID: {warehouse_id}")
                return None
            return Warehouse.model_validate(warehouse_db)
        except SQLAlchemyError as e:
            print(f"Error fetching warehouse: {e}")
            return None

    def list_all(self) -> List[Warehouse]:
        try:
            warehouses_db = self.session.query(WarehouseModel).all()
            return [Warehouse.model_validate(w) for w in warehouses_db]
        except SQLAlchemyError as e:
            print(f"Error listing warehouses: {e}")
            return []

    def update(self, warehouse_id: int, new_address: str = None, new_name: str = None) -> Optional[Warehouse]:
        try:
            warehouse_db = self.session.get(WarehouseModel, warehouse_id)
            if not warehouse_db:
                print(f"No warehouse found with ID: {warehouse_id}")
                return None
            if new_address:
                warehouse_db.warehouse_address = new_address
            if new_name:
                warehouse_db.warehouse_name = new_name
            self.session.commit()
            self.session.refresh(warehouse_db)
            return Warehouse.model_validate(warehouse_db)
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error updating warehouse: {e}")
            return None

    def delete(self, warehouse_id: int) -> bool:
        try:
            warehouse_db = self.session.get(WarehouseModel, warehouse_id)
            if not warehouse_db:
                print(f"No warehouse found with ID: {warehouse_id}")
                return False
            self.session.delete(warehouse_db)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error deleting warehouse: {e}")
            return False