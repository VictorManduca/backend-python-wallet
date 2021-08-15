from fastapi import FastAPI

from src.core.settings import settings
from src.database.connection import engine
from src.database.models.base_model import Base
from src.routes import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_routes(server_instance: FastAPI):
    server_instance.include_router(api_router)


def start_up():
    server_instance = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_routes(server_instance)
    create_tables()

    return server_instance


app = start_up()
