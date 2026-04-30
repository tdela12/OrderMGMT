import pytest
from sqlalchemy.exc import IntegrityError
from services.database.app.db import Customer, Product, Warehouse, Order, Inventory


# ─────────────────────────────────────────────
# CUSTOMER TESTS
# ─────────────────────────────────────────────

class TestCustomerCRUD:

    def test_add_customer(self, session):
        customer = Customer(customer_name="Bob Jones", customer_address="789 Elm St")
        session.add(customer)
        session.flush()

        assert customer.customer_id is not None
        assert customer.customer_name == "Bob Jones"
        assert customer.customer_address == "789 Elm St"

    def test_get_customer(self, session, sample_customer):
        fetched = session.get(Customer, sample_customer.customer_id)
        assert fetched.customer_name == "Alice Smith"

    def test_get_customer_not_found(self, session):
        result = session.get(Customer, 99999)
        assert result is None

    def test_update_customer_name(self, session, sample_customer):
        sample_customer.customer_name = "Alice Johnson"
        session.flush()

        updated = session.get(Customer, sample_customer.customer_id)
        assert updated.customer_name == "Alice Johnson"
        assert updated.customer_address == "123 Main St"  # unchanged

    def test_update_customer_address(self, session, sample_customer):
        sample_customer.customer_address = "999 New Ave"
        session.flush()

        updated = session.get(Customer, sample_customer.customer_id)
        assert updated.customer_address == "999 New Ave"

    def test_delete_customer(self, session, sample_customer):
        customer_id = sample_customer.customer_id
        session.delete(sample_customer)
        session.flush()

        assert session.get(Customer, customer_id) is None

    def test_customer_name_required(self, session):
        with pytest.raises(IntegrityError):
            session.add(Customer(customer_name=None, customer_address="123 St"))
            session.flush()

    def test_customer_address_required(self, session):
        with pytest.raises(IntegrityError):
            session.add(Customer(customer_name="No Address", customer_address=None))
            session.flush()


# ─────────────────────────────────────────────
# PRODUCT TESTS
# ─────────────────────────────────────────────

class TestProductCRUD:

    def test_add_product(self, session):
        product = Product(product_name="Gadget")
        session.add(product)
        session.flush()

        assert product.product_id is not None
        assert product.product_name == "Gadget"

    def test_get_product_by_id(self, session, sample_product):
        fetched = session.get(Product, sample_product.product_id)
        assert fetched.product_name == "Widget"

    def test_get_product_by_name(self, session, sample_product):
        fetched = session.query(Product).filter_by(product_name="Widget").first()
        assert fetched.product_id == sample_product.product_id

    def test_get_product_not_found(self, session):
        result = session.query(Product).filter_by(product_name="Nonexistent").first()
        assert result is None

    def test_update_product_name(self, session, sample_product):
        sample_product.product_name = "Super Widget"
        session.flush()

        updated = session.get(Product, sample_product.product_id)
        assert updated.product_name == "Super Widget"

    def test_delete_product(self, session, sample_product):
        product_id = sample_product.product_id
        session.delete(sample_product)
        session.flush()

        assert session.get(Product, product_id) is None


# ─────────────────────────────────────────────
# WAREHOUSE TESTS
# ─────────────────────────────────────────────

class TestWarehouseCRUD:

    def test_add_warehouse(self, session):
        warehouse = Warehouse(warehouse_name="Warehouse B", warehouse_address="101 Dock Lane")
        session.add(warehouse)
        session.flush()

        assert warehouse.warehouse_id is not None
        assert warehouse.warehouse_name == "Warehouse B"

    def test_get_warehouse(self, session, sample_warehouse):
        fetched = session.get(Warehouse, sample_warehouse.warehouse_id)
        assert fetched.warehouse_name == "Warehouse A"

    def test_get_warehouse_not_found(self, session):
        result = session.get(Warehouse, 99999)
        assert result is None

    def test_update_warehouse(self, session, sample_warehouse):
        sample_warehouse.warehouse_address = "999 New Dock Rd"
        session.flush()

        updated = session.get(Warehouse, sample_warehouse.warehouse_id)
        assert updated.warehouse_address == "999 New Dock Rd"

    def test_delete_warehouse(self, session, sample_warehouse):
        warehouse_id = sample_warehouse.warehouse_id
        session.delete(sample_warehouse)
        session.flush()

        assert session.get(Warehouse, warehouse_id) is None

    def test_warehouse_address_required(self, session):
        with pytest.raises(IntegrityError):
            session.add(Warehouse(warehouse_name="No Address", warehouse_address=None))
            session.flush()


# ─────────────────────────────────────────────
# ORDER TESTS
# ─────────────────────────────────────────────

class TestOrderCRUD:

    def test_add_order(self, session, sample_customer, sample_product):
        order = Order(
            customer_id=sample_customer.customer_id,
            product_id=sample_product.product_id,
            quantity=5,
            status="pending"
        )
        session.add(order)
        session.flush()

        assert order.order_id is not None
        assert order.quantity == 5
        assert order.status == "pending"

    def test_get_order(self, session, sample_order):
        fetched = session.get(Order, sample_order.order_id)
        assert fetched.quantity == 3
        assert fetched.status == "pending"

    def test_get_order_not_found(self, session):
        result = session.get(Order, 99999)
        assert result is None

    def test_update_order_status(self, session, sample_order):
        sample_order.status = "shipped"
        session.flush()

        updated = session.get(Order, sample_order.order_id)
        assert updated.status == "shipped"
        assert updated.quantity == 3  # unchanged

    def test_update_order_quantity(self, session, sample_order):
        sample_order.quantity = 10
        session.flush()

        updated = session.get(Order, sample_order.order_id)
        assert updated.quantity == 10

    def test_delete_order(self, session, sample_order):
        order_id = sample_order.order_id
        session.delete(sample_order)
        session.flush()

        assert session.get(Order, order_id) is None

    def test_order_invalid_customer_fk(self, session, sample_product):
        """Order must reference a real customer."""
        with pytest.raises(IntegrityError):
            session.add(Order(
                customer_id=99999,
                product_id=sample_product.product_id,
                quantity=1,
                status="pending"
            ))
            session.flush()

    def test_order_invalid_product_fk(self, session, sample_customer):
        """Order must reference a real product."""
        with pytest.raises(IntegrityError):
            session.add(Order(
                customer_id=sample_customer.customer_id,
                product_id=99999,
                quantity=1,
                status="pending"
            ))
            session.flush()


# ─────────────────────────────────────────────
# INVENTORY TESTS
# ─────────────────────────────────────────────

class TestInventoryCRUD:

    def test_add_inventory(self, session, sample_product, sample_warehouse):
        inventory = Inventory(
            product_id=sample_product.product_id,
            warehouse_id=sample_warehouse.warehouse_id,
            quantity=200
        )
        session.add(inventory)
        session.flush()

        assert inventory.inventory_id is not None
        assert inventory.quantity == 200

    def test_get_inventory(self, session, sample_inventory):
        fetched = session.query(Inventory).filter_by(
            product_id=sample_inventory.product_id,
            warehouse_id=sample_inventory.warehouse_id
        ).first()
        assert fetched.quantity == 100

    def test_get_inventory_not_found(self, session):
        result = session.query(Inventory).filter_by(product_id=99999, warehouse_id=99999).first()
        assert result is None

    def test_update_inventory_quantity(self, session, sample_inventory):
        sample_inventory.quantity = 250
        session.flush()

        updated = session.get(Inventory, sample_inventory.inventory_id)
        assert updated.quantity == 250

    def test_delete_inventory(self, session, sample_inventory):
        inventory_id = sample_inventory.inventory_id
        session.delete(sample_inventory)
        session.flush()

        assert session.get(Inventory, inventory_id) is None

    def test_inventory_invalid_product_fk(self, session, sample_warehouse):
        """Inventory must reference a real product."""
        with pytest.raises(IntegrityError):
            session.add(Inventory(
                product_id=99999,
                warehouse_id=sample_warehouse.warehouse_id,
                quantity=10
            ))
            session.flush()

    def test_inventory_invalid_warehouse_fk(self, session, sample_product):
        """Inventory must reference a real warehouse."""
        with pytest.raises(IntegrityError):
            session.add(Inventory(
                product_id=sample_product.product_id,
                warehouse_id=99999,
                quantity=10
            ))
            session.flush()