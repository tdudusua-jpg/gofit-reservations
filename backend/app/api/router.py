from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.reservations import router as reservations_router

api_router = APIRouter()

api_router.include_router(health_router, tags=["Health"])
api_router.include_router(reservations_router, tags=["Reservations"])