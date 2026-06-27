from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from backend.app.database.base import Base


class Recommendation(Base):

    __tablename__ = "recommendations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    prediction_id = Column(
        Integer,
        ForeignKey("predictions.id"),
        nullable=False
    )

    disease_name = Column(
        String,
        nullable=False
    )

    severity = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=False
    )

    treatment = Column(
        String,
        nullable=False
    )

    organic_treatment = Column(
        String,
        nullable=True
    )

    chemical_treatment = Column(
        String,
        nullable=True
    )

    preventive_measures = Column(
        String,
        nullable=True
    )

    monitoring_actions = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    prediction = relationship(
        "Prediction",
        back_populates="recommendation"
    )