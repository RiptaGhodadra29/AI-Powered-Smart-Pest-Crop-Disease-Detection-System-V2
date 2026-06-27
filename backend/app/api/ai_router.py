from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.app.database.session import get_db

from backend.app.schemas.ai_router_schema import (
    AIRouterRequest
)

from backend.app.services.ai_router_service import (
    AIRouterService
)


router = APIRouter()

service = AIRouterService()


@router.post("/predict")
def predict_image(
    request: AIRouterRequest,
    db: Session = Depends(get_db)
):

    result = service.route_image(
        db=db,
        user_id=request.user_id,
        image_id=request.image_id,
        image_type=request.image_type
    )

    if result is None:

        raise HTTPException(
            status_code=404,
            detail="Image not found"
        )

    return result