from database.app.inventory_operations import add_inventory, get_inventory


# Update inventory
# Check inventory
# Out of stock logic


def available_to_sell(product_id: int, warehouse_id: int) -> bool:
     inventory = get_inventory(product_id, warehouse_id)
     return inventory.quantity > 0
