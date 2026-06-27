from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from backend.app.database.base import Base


class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    image_id = Column(
        Integer,
        ForeignKey("uploaded_images.id"),
        nullable=False
    )

    prediction_type = Column(
        String,
        nullable=False
    )

    model_name = Column(
        String,
        nullable=False
    )

    class_id = Column(
        Integer,
        nullable=False
    )

    class_name = Column(
        String,
        nullable=False
    )

    confidence = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="predictions"
    )

    image = relationship(
        "UploadedImage",
        back_populates="predictions"
    )
    recommendation = relationship(
    "Recommendation",
    back_populates="prediction",
    uselist=False
)