from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from src.database.models.base_model import Base


class Api_Request(Base):
    id = Column(Integer, primary_key=True, index=True)
    sold_at = Column(Date, nullable=False)
    customer_document = Column(String(100), nullable=False)
    customer_name = Column(String(100), nullable=False)
    total_value = Column(Numeric, nullable=False)
