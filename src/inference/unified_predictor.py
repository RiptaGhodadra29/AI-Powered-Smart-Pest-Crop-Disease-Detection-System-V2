from src.inference.disease_predictor import (
    DiseasePredictor
)


class UnifiedPredictor:
    """
    Central prediction interface.
    """

    def __init__(self):

        self.disease_predictor = (
            DiseasePredictor()
        )

    def predict_disease(
        self,
        image_path
    ):
        """
        Disease prediction.
        """

        return self.disease_predictor.predict(
            image_path
        )