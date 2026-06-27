from src.inference.unified_predictor import (
    UnifiedPredictor
)

from src.pest_detection.pest_recommendation_pipeline import (
    PestRecommendationPipeline
)


class AIRouter:
    """
    Central AI Router
    """

    def __init__(self):

        self.disease_predictor = (
            UnifiedPredictor()
        )

        self.pest_pipeline = (
            PestRecommendationPipeline()
        )

    def predict_disease(
        self,
        image_path
    ):

        return self.disease_predictor.predict_disease(
            image_path
        )

    def predict_pest(
        self,
        image_path
    ):

        return self.pest_pipeline.process_image(
            image_path
        )