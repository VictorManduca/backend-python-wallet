from sqlalchemy.orm import Session

from src.database.models.api_request_model import Api_Request
from src.database.models.api_response_model import Api_Response
from src.dtos.requests.cashback_request import CashbackCreatePayload


def create_api_request(payload: Api_Request, database: Session):
    cashback_request = Api_Request(**payload)

    database.add(cashback_request)
    database.commit()
    database.refresh(cashback_request)

    return cashback_request


def create_cashback_response(payload: Api_Response, database: Session):
    api_response = Api_Response(**payload)

    database.add(api_response)
    database.commit()
    database.refresh(api_response)

    return api_response
