from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.app.database.session import get_db

from backend.app.services.history_service import (
    get_user_history
)

from backend.app.schemas.prediction_schema import (
    PredictionHistoryResponse
)

router = APIRouter()


@router.get(
    "/{user_id}",
    response_model=PredictionHistoryResponse
)
def history_api(
    user_id: int,
    db: Session = Depends(get_db)
):

    predictions = get_user_history(
        db,
        user_id
    )

    history = []

    for prediction in predictions:

        history.append(
    {
        "prediction_id": prediction.id,
        "class_name": prediction.class_name,
        "confidence": prediction.confidence,
        "model_name": prediction.model_name,
        "prediction_type": prediction.prediction_type,
        "created_at": prediction.created_at
    }
)

    return {
        "history": history
    }