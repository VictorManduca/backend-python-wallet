from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.core.security import create_access_token
from src.core.settings import settings
from src.services import rest_service

router = APIRouter()


@router.post('/login', status_code=status.HTTP_200_OK, summary='Login')
def login(payload: OAuth2PasswordRequestForm = Depends()):
    try:
        if payload.username == settings.VALID_USERNAME and payload.password == settings.VALID_PASSWORD:
            token = create_access_token(payload.__dict__)

            return {
                'access_token': token,
                'token_type': 'bearer'
            }
        else:
            raise Exception('Invalid email or password')
    except BaseException as exception:
        raise rest_service.bad_request('[auth|controller] {}'.format(exception))
