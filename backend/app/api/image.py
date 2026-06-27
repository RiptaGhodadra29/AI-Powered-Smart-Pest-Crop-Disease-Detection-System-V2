from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile

from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.image_schema import ImageUploadResponse
from backend.app.services.image_service import save_image


router = APIRouter()


@router.post(
    "/upload",
    response_model=ImageUploadResponse
)
def upload_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    image_record = save_image(
        db=db,
        user_id=1,
        file=file
    )

    return {
        "image_id": image_record.id,
        "image_name": image_record.image_name,
        "image_path": image_record.image_path
    }