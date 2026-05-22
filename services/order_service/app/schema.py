from pydantic import BaseModel
from utils.enums import Status

class Order(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    status: Status
    
    class Config:
        from_attributes = True