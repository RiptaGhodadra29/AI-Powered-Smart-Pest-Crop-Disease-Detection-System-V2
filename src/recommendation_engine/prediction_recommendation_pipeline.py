from src.recommendation_engine.class_name_mapper import (
    map_disease_name
)

from src.recommendation_engine.recommendation_service import (
    RecommendationService
)


class PredictionRecommendationPipeline:

    def __init__(self):
        self.service = RecommendationService()

    def get_disease_recommendation(
        self,
        predicted_class
    ):

        # Unknown crop
        if predicted_class == "Unknown_Crop":
            return {
                "status": "unknown",
                "message": (
                    "Unsupported crop detected."
                )
            }

        # Healthy classes from dataset
        HEALTHY_CLASSES = {
            "Apple_Leaf",
            "Bell_Pepper_Leaf",
            "Blueberry_Leaf",
            "Cherry_Leaf",
            "Grape_Leaf",
            "Peach_Leaf",
            "Raspberry_Leaf",
            "Soyabean_Leaf",
            "Strawberry_Leaf",
            "Tomato_Leaf",
        }

        # Healthy crops
        if (
            "healthy" in predicted_class.lower()
            or predicted_class in HEALTHY_CLASSES
        ):
            return {
                "status": "healthy",
                "message": (
                    "No disease detected. Crop appears healthy."
                )
            }

        disease_name = map_disease_name(
            predicted_class
        )

        if disease_name is None:
            return {
                "status": "error",
                "message": (
                    f"No mapping found for "
                    f"{predicted_class}"
                )
            }

        return self.service.process_disease(
            disease_name
        )