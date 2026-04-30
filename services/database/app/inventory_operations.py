from sqlalchemy.exc import SQLAlchemyError
from db import get_session, Inventory


def add_inventory(product_id: int, warehouse_id: int, quantity: int):
    """Add a new inventory record."""
    session = get_session()
    try:
        inventory = Inventory(product_id=product_id, warehouse_id=warehouse_id, quantity=quantity)
        session.add(inventory)
        session.commit()
        session.refresh(inventory)
        print(f"Inventory added with ID: {inventory.inventory_id}")
        return inventory
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding inventory: {e}")
    finally:
        session.close()


def get_inventory(product_id: int, warehouse_id: int):
    """Fetch an inventory record by product and warehouse."""
    session = get_session()
    try:
        inventory = (
            session.query(Inventory)
            .filter_by(product_id=product_id, warehouse_id=warehouse_id)
            .first()
        )
        if not inventory:
            print(f"No inventory found for product {product_id} in warehouse {warehouse_id}")
        return inventory
    except SQLAlchemyError as e:
        print(f"Error fetching inventory: {e}")
    finally:
        session.close()


def update_inventory(product_id: int, warehouse_id: int, new_quantity: int):
    """Update quantity for a given product and warehouse."""
    session = get_session()
    try:
        inventory = (
            session.query(Inventory)
            .filter_by(product_id=product_id, warehouse_id=warehouse_id)
            .first()
        )
        if not inventory:
            print(f"No inventory found for product {product_id} in warehouse {warehouse_id}")
            return None
        inventory.quantity = new_quantity
        session.commit()
        session.refresh(inventory)
        return inventory
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error updating inventory: {e}")
    finally:
        session.close()


def delete_inventory(product_id: int, warehouse_id: int):
    """Delete an inventory record by product and warehouse."""
    session = get_session()
    try:
        inventory = (
            session.query(Inventory)
            .filter_by(product_id=product_id, warehouse_id=warehouse_id)
            .first()
        )
        if not inventory:
            print(f"No inventory found for product {product_id} in warehouse {warehouse_id}")
            return False
        session.delete(inventory)
        session.commit()
        print(f"Inventory for product {product_id} in warehouse {warehouse_id} deleted.")
        return True
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error deleting inventory: {e}")
    finally:
        session.close()
