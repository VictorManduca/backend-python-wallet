from datetime import date, datetime
from typing import List

from pydantic import BaseModel

from src.dtos.requests.customer_request import Customer
from src.dtos.requests.product_request import Product


class CashbackCreatePayload(BaseModel):
    sold_at: str = datetime.now().replace(microsecond=0).isoformat(' ')
    customer: Customer
    total: str
    products: List[Product]
