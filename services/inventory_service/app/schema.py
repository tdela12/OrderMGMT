from pydantic import BaseModel

class Inventory(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: int
    
    class Config:
        from_attributes = True
        
        