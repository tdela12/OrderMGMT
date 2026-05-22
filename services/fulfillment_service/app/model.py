from sqlalchemy import Column, Integer, String
from db.py import Base

class Warehouse(Base):
    __tablename__ = "warehouses"

    warehouse_id = Column(Integer, primary_key=True, autoincrement=True)
    warehouse_address = Column(String(255), nullable=False)
    warehouse_name = Column(String(255))