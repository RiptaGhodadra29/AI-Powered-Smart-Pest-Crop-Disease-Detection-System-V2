from pydantic import BaseModel


class ImageUploadResponse(BaseModel):
    image_id: int
    image_name: str
    image_path: str

    class Config:
        from_attributes = True