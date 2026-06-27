import os
import uuid

from sqlalchemy.orm import Session

from backend.app.models.uploaded_image import UploadedImage


UPLOAD_DIR = "backend/uploads/images"


def save_image(
    db: Session,
    user_id: int,
    file
):
    # Generate unique filename

    file_extension = file.filename.split(".")[-1]

    unique_filename = (
        f"{uuid.uuid4()}.{file_extension}"
    )

    file_path = os.path.join(
        UPLOAD_DIR,
        unique_filename
    )

    # Save image to disk

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Save record to database

    image_record = UploadedImage(
        user_id=user_id,
        image_name=file.filename,
        image_path=file_path
    )

    db.add(image_record)
    db.commit()
    db.refresh(image_record)

    return image_record