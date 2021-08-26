import os
import sys
from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database.models.base_model import Base
from src.routes import api_router
from src.database.connection import get_database
from src.core.settings import settings


def start_application():
    app = FastAPI()
    app.include_router(api_router)
    return app


engine = create_engine(settings.DATABASE_URL)
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def app() -> Generator[FastAPI, Any, None]:
    _app = start_application()
    yield _app


@pytest.fixture(scope="module")
def database_connection(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)

    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="module")
def client(app: FastAPI, database_connection: SessionTesting) -> Generator[TestClient, Any, None]:
    def _get_test_database():
        try:
            yield database_connection
        finally:
            pass

    app.dependency_overrides[get_database] = _get_test_database
    with TestClient(app) as client:
        yield client
