from pydantic import BaseModel


class DashboardResponse(BaseModel):
    user_id: int
    total_predictions: int
    most_detected_disease: str
    average_confidence: float