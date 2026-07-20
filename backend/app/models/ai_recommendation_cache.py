from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Text

from backend.app.database.base import Base


class AIRecommendationCache(Base):

    __tablename__ = "ai_recommendation_cache"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    disease_name = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    recommendation_json = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )