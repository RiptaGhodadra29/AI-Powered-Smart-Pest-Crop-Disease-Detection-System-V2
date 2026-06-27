from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.app.database.session import get_db

from backend.app.schemas.prediction_schema import (
    PredictionRequest,
    PredictionResponse
)

from backend.app.services.prediction_service import (
    create_prediction
)

router = APIRouter()


@router.post(
    "/disease",
    response_model=PredictionResponse
)
def predict_disease_api(
    request: PredictionRequest,
    db: Session = Depends(get_db)
):

    result = create_prediction(
        db=db,
        user_id=request.user_id,
        image_id=request.image_id
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Image not found"
        )

    prediction = result["prediction"]

    recommendation = result["recommendation"]

    return {
    "prediction_id": prediction.id,
    "class_name": prediction.class_name,
    "confidence": prediction.confidence,
    "model_name": prediction.model_name,
    "recommendation": recommendation,
    "confidence_level": result["confidence_level"]
}