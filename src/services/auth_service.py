from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from src.core.settings import settings
from src.services import rest_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


def get_user_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("username")
        password: str = payload.get("password")

        if username is None or password is None:
            raise rest_service.unauthorized()

        if not username == settings.VALID_USERNAME and not password == settings.VALID_PASSWORD:
            raise rest_service.unauthorized()

        return {'username': username}
    except BaseException:
        raise rest_service.unauthorized()
