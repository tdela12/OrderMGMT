from pydantic import BaseModel

class Warehouse(BaseModel):
    warehouse_id: int
    warehouse_address: str
    warehouse_name: str
    
    class Config:
        from_attributes = True
        
        