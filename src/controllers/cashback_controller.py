from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.database.connection import get_database
from src.dtos.requests.cashback_request import CashbackCreatePayload
from src.services import cashback_service
from src.services import rest_service

router = APIRouter()


@router.post('/cashback', status_code=status.HTTP_201_CREATED, summary='Create and calculate a cashback')
def calculate_cashback(payload: CashbackCreatePayload, database: Session = Depends(get_database)):
    try:
        saved_cashback_request = cashback_service.calculate_cashback(payload, database)
        return saved_cashback_request
    except BaseException as exception:
        raise rest_service.bad_request('[cashback|controller] {}'.format(exception))
