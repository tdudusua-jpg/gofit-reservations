from datetime import datetime

from pydantic import BaseModel


class ReservationCreate(BaseModel):
    gofit_class_id: str
    class_name: str
    starts_at: datetime


class ReservationResponse(BaseModel):
    id: int
    gofit_class_id: str
    class_name: str
    starts_at: datetime
    status: str
    created_at: datetime