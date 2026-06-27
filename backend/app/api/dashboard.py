from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.app.database.session import get_db

from backend.app.services.dashboard_service import (
    get_dashboard_data
)

from backend.app.schemas.dashboard_schema import (
    DashboardResponse
)

router = APIRouter()


@router.get(
    "/{user_id}",
    response_model=DashboardResponse
)
def dashboard_api(
    user_id: int,
    db: Session = Depends(get_db)
):

    return get_dashboard_data(
        db,
        user_id
    )