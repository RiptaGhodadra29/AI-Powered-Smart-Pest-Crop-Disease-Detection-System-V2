"""
Recommendation Service

Central controller for the Recommendation Engine.
"""

from .disease_recommender import DiseaseRecommender
from .pest_recommender import PestRecommender
from .farmer_message_generator import FarmerMessageGenerator


class RecommendationService:

    def __init__(self):

        self.disease_recommender = DiseaseRecommender()
        self.pest_recommender = PestRecommender()
        self.message_generator = FarmerMessageGenerator()

    def process_disease(self, disease_name: str):

        # Unknown crop support
        if disease_name == "Unknown_Crop":

            return {
                "status": "unknown_crop",
                "message": (
                    "The uploaded image does not belong to any crop "
                    "currently supported by the system."
                )
            }

        # Healthy crop support
        if "healthy" in disease_name.lower():

            return {
                "status": "healthy",
                "message": (
                    "The crop appears healthy. "
                    "No disease symptoms detected."
                )
            }

        recommendation = (
            self.disease_recommender
            .get_recommendation(disease_name)
        )

        return self.message_generator.generate_disease_message(
            recommendation
        )

    def process_pest(self, pest_name: str):

        recommendation = (
            self.pest_recommender
            .get_recommendation(pest_name)
        )

        return self.message_generator.generate_pest_message(
            recommendation
        )

    def process_prediction(
        self,
        prediction_type: str,
        prediction_name: str
    ):

        prediction_type = prediction_type.lower()

        if prediction_type == "disease":

            return self.process_disease(
                prediction_name
            )

        elif prediction_type == "pest":

            return self.process_pest(
                prediction_name
            )

        return self.message_generator.generate_unknown_message()