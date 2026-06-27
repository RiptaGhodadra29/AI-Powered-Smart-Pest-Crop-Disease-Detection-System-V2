from .pest_predictor import PestPredictor

from src.recommendation_engine.recommendation_service import (
    RecommendationService
)


class PestRecommendationPipeline:

    def __init__(self):

        self.predictor = PestPredictor()

        self.service = RecommendationService()

    def process_image(self, image_path):

        prediction = self.predictor.predict(
            image_path
        )

        if prediction is None:

            return {
                "status": "no_pest_detected"
            }

        return self.service.process_pest(
            prediction["pest_name"]
        )