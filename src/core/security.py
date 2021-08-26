from datetime import datetime, timedelta
from typing import Optional

from jose import jwt

from src.core.settings import settings


def create_access_token(encode_data):
    expire = (datetime.utcnow() + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))).isoformat()
    encode_data.update({"expiresIn": expire})

    return jwt.encode(encode_data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
