from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.database.database import get_db
from app.infrastructure.database.reservation_model import ReservationModel
from app.schemas.reservation import ReservationCreate, ReservationResponse

router = APIRouter()


@router.post(
    "/reservations",
    response_model=ReservationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_reservation(
    reservation: ReservationCreate,
    db: Session = Depends(get_db),
):
    new_reservation = ReservationModel(
        gofit_class_id=reservation.gofit_class_id,
        class_name=reservation.class_name,
        starts_at=reservation.starts_at,
    )

    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)

    return new_reservation


@router.get(
    "/reservations",
    response_model=list[ReservationResponse],
)
def get_reservations(db: Session = Depends(get_db)):
    statement = select(ReservationModel)

    reservations = db.scalars(statement).all()

    return reservations