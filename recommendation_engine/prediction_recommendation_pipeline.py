from .class_mapping import CLASS_MAPPING
from .recommendation_service import RecommendationService


class PredictionRecommendationPipeline:

    def __init__(self):
        self.service = RecommendationService()

    def get_disease_recommendation(
        self,
        predicted_class
    ):

        mapped_class = CLASS_MAPPING.get(
            predicted_class
        )

        if mapped_class == "healthy":
            return {
                "status": "healthy",
                "message":
                "No disease detected. Crop appears healthy."
            }

        if mapped_class == "unknown":
            return {
                "status": "unknown",
                "message":
                "Unsupported crop detected."
            }

        return self.service.process_disease(
            mapped_class
        )