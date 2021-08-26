from fastapi import APIRouter

from src.controllers import auth_controller
from src.controllers import cashback_controller

api_router = APIRouter()

api_router.include_router(auth_controller.router, prefix='/api', tags=['Auth'])
api_router.include_router(cashback_controller.router, prefix='/api', tags=['Cashback'])
