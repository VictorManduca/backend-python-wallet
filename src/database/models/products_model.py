from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from src.database.models.base_model import Base


class Products(Base):
    id = Column(Integer, primary_key=True, index=True)
    cashback_id = Column(Integer, ForeignKey("api_request.id"))
    type = Column(String(100), nullable=False)
    value = Column(Numeric, nullable=False)
    qty = Column(Integer, nullable=False)

    cashback_relation = relationship("Api_Request")
