from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id : int
    name : str
    address : Optional[str]
    cellphone : int
    created_at : datetime = datetime.now()