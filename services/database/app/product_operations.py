from sqlalchemy.exc import SQLAlchemyError
from db import get_session, Product


def add_product(product_name: str):
    """Add a new product."""
    session = get_session()
    try:
        product = Product(product_name=product_name)
        session.add(product)
        session.commit()
        session.refresh(product)
        print(f"Product added with ID: {product.product_id}")
        return product
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding product: {e}")
    finally:
        session.close()


def get_product(product_name: str):
    """Fetch a product by name."""
    session = get_session()
    try:
        product = session.query(Product).filter_by(product_name=product_name).first()
        if not product:
            print(f"No product found with name: {product_name}")
        return product
    except SQLAlchemyError as e:
        print(f"Error fetching product: {e}")
    finally:
        session.close()


def get_product_by_id(product_id: int):
    """Fetch a product by ID."""
    session = get_session()
    try:
        product = session.get(Product, product_id)
        if not product:
            print(f"No product found with ID: {product_id}")
        return product
    except SQLAlchemyError as e:
        print(f"Error fetching product: {e}")
    finally:
        session.close()


def update_product(product_name: str, new_product_name: str):
    """Update a product's name."""
    session = get_session()
    try:
        product = session.query(Product).filter_by(product_name=product_name).first()
        if not product:
            print(f"No product found with name: {product_name}")
            return None
        product.product_name = new_product_name
        session.commit()
        session.refresh(product)
        return product
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error updating product: {e}")
    finally:
        session.close()


def delete_product(product_name: str):
    """Delete a product by name."""
    session = get_session()
    try:
        product = session.query(Product).filter_by(product_name=product_name).first()
        if not product:
            print(f"No product found with name: {product_name}")
            return False
        session.delete(product)
        session.commit()
        print(f"Product '{product_name}' deleted.")
        return True
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error deleting product: {e}")
    finally:
        session.close()