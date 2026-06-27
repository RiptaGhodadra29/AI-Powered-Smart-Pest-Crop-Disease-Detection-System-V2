from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.app.database.session import get_db

from backend.app.models.uploaded_image import UploadedImage

from backend.app.services.pest_detection_service import (
    detect_pests
)

router = APIRouter()


@router.post("/pest/{image_id}")
def detect_pest_api(
    image_id: int,
    db: Session = Depends(get_db)
):

    image = (
        db.query(UploadedImage)
        .filter(
            UploadedImage.id == image_id
        )
        .first()
    )

    if not image:
        raise HTTPException(
            status_code=404,
            detail="Image not found"
        )

    detections = detect_pests(
        image.image_path
    )

    return {
        "image_id": image.id,
        "image_name": image.image_name,
        "total_detections": len(
            detections
        ),
        "detections": detections
    }