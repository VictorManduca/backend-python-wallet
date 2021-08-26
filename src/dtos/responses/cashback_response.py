from pydantic import BaseModel


class CashbackResponse(BaseModel):
    id: int
    cashback_id: str
    document: str
    cashback: str
    createdAt: str
