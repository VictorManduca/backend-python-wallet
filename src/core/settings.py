import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "Backend Python Wallet"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_USER: str = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT", 3306)
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "walletDB")
    DATABASE_URL: str = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

    MAISTODOS_URL: str = os.getenv("MAISTODOS_URL")

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    VALID_EMAIL: str = "mais_tod@s.com"
    VALID_PASSWORD: str = "MeContrataNaHumilda"


settings = Settings()
