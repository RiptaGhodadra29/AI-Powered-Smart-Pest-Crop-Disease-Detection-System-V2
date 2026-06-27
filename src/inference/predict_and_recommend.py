from src.inference.unified_predictor import UnifiedPredictor


class PredictAndRecommend:

    def __init__(self):
        self.predictor = UnifiedPredictor()

    def process_image(self, image_path):

        result = self.predictor.predict_disease(
            image_path
        )

        return result