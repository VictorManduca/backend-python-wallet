from pydantic import BaseModel


class Customer(BaseModel):
    document: str
    name: str
