from datetime import timedelta

from fastapi import APIRouter, status

from src.core.security import create_access_token
from src.core.settings import settings
from src.dtos.requests.auth_request import AuthRequest
from src.services import rest_service

router = APIRouter()


@router.post('/login', status_code=status.HTTP_200_OK, summary='Login')
def login(payload: AuthRequest):
    try:
        if payload.email == settings.VALID_EMAIL and payload.password == settings.VALID_PASSWORD:
            token = create_access_token(payload.__dict__)

            return {
                'token': token,
                'token_type': 'bearer'
            }
        else:
            raise Exception('Invalid email or password')
    except BaseException as exception:
        raise rest_service.bad_request('[auth|controller] {}'.format(exception))
