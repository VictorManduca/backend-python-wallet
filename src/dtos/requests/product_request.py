from pydantic import BaseModel


class Product(BaseModel):
    type: str
    value: str
    qty: int
