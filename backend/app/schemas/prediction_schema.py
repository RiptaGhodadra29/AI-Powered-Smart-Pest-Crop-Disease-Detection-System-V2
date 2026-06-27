from pydantic import BaseModel
from typing import List
from datetime import datetime


class PredictionRequest(BaseModel):
    user_id: int
    image_id: int


class RecommendationResponse(BaseModel):
    disease_name: str
    severity: str
    description: str
    treatment: str
    organic_treatment: str
    chemical_treatment: str
    preventive_measures: str
    monitoring_actions: str


class PredictionResponse(BaseModel):
    prediction_id: int
    class_name: str
    confidence: float
    confidence_level: str
    model_name: str
    recommendation: RecommendationResponse


class PredictionHistoryItem(BaseModel):
    prediction_id: int
    class_name: str
    confidence: float
    model_name: str
    prediction_type: str
    created_at: datetime


class PredictionHistoryResponse(BaseModel):
    history: List[PredictionHistoryItem]