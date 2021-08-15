from sqlalchemy import Column, Date, Integer, String

from src.database.models.base_model import Base


class Api_Response(Base):
    id = Column(Integer, primary_key=True, index=True)
    createdAt = Column(Date, nullable=False)
    cashback_id = Column(String(100), nullable=False)
    document = Column(String(100), nullable=False)
    cashback = Column(String(100), nullable=False)
