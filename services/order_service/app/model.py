from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from utils.enums import Status


Base = declarative_base()

class OrderModel(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(Enum(Status), nullable=False)