"""
Disease Recommender

Retrieves disease recommendations from the
Disease Knowledge Base.

Author: AI-Powered Smart Pest & Crop Disease Detection System
"""

from .knowledge_base_loader import KnowledgeBaseLoader
from .translator import RecommendationTranslator


class DiseaseRecommender:
    """
    Handles disease recommendation retrieval.
    """

    def __init__(self):

        self.loader = KnowledgeBaseLoader()

        self.translator = (
            RecommendationTranslator()
        )

        self.disease_df = (
            self.loader.load_disease_kb()
        )

    def validate_disease(
        self,
        disease_name: str
    ) -> bool:
        """
        Check if disease exists.
        """

        matches = self.disease_df[
            self.disease_df["disease_name"]
            .str.lower()
            .str.strip()
            == disease_name.lower().strip()
        ]

        return not matches.empty

    def find_disease(
        self,
        disease_name: str
    ):
        """
        Search disease by name.
        """

        matches = self.disease_df[
            self.disease_df["disease_name"]
            .str.lower()
            .str.strip()
            == disease_name.lower().strip()
        ]

        if matches.empty:
            return None

        return matches.iloc[0]

    def get_recommendation(
        self,
        disease_name: str,
        language: str = "en"
    ):
        """
        Retrieve complete disease record.
        """

        disease_record = self.find_disease(
            disease_name
        )

        if disease_record is None:
            return {
                "status": "error",
                "message": (
                    f"Disease recommendation not found: "
                    f"{disease_name}"
                )
            }

        recommendation = {
            "status": "success",
            "disease_id": disease_record["disease_id"],
            "disease_name": disease_record["disease_name"],
            "severity_level": disease_record["severity_level"],
            "description": disease_record["description"],
            "treatment": disease_record["treatment"],
            "organic_treatment": disease_record["organic_treatment"],
            "chemical_treatment": disease_record["chemical_treatment"],
            "preventive_measures": disease_record["preventive_measures"],
            "monitoring_actions": disease_record["monitoring_actions"]
        }

        if language != "en":

            recommendation["description"] = (
                self.translator.translate_text(
                    recommendation["description"],
                    language
                )
            )

            recommendation["treatment"] = (
                self.translator.translate_text(
                    recommendation["treatment"],
                    language
                )
            )

            recommendation["organic_treatment"] = (
                self.translator.translate_text(
                    recommendation["organic_treatment"],
                    language
                )
            )

            recommendation["chemical_treatment"] = (
                self.translator.translate_text(
                    recommendation["chemical_treatment"],
                    language
                )
            )

            recommendation["preventive_measures"] = (
                self.translator.translate_text(
                    recommendation["preventive_measures"],
                    language
                )
            )

            recommendation["monitoring_actions"] = (
                self.translator.translate_text(
                    recommendation["monitoring_actions"],
                    language
                )
            )

        return recommendation