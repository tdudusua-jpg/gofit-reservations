from fastapi import FastAPI

from app.api.router import api_router
from app.infrastructure.database.database import Base, engine
from app.infrastructure.database.reservation_model import ReservationModel

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GO fit Reservations API",
    version="0.1.0",
)

app.include_router(api_router)