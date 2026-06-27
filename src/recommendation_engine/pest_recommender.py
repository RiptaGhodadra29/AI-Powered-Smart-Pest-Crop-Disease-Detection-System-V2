"""
Pest Recommender

Retrieves pest recommendations from the
Pest Knowledge Base.
"""

from .knowledge_base_loader import KnowledgeBaseLoader


class PestRecommender:
    """
    Handles pest recommendation retrieval.
    """

    def __init__(self):
        self.loader = KnowledgeBaseLoader()
        self.pest_df = self.loader.load_pest_kb()

    def validate_pest(self, pest_name: str) -> bool:

        matches = self.pest_df[
            self.pest_df["pest_name"]
            .str.lower()
            .str.strip()
            == pest_name.lower().strip()
        ]

        return not matches.empty

    def find_pest(self, pest_name: str):

        matches = self.pest_df[
            self.pest_df["pest_name"]
            .str.lower()
            .str.strip()
            == pest_name.lower().strip()
        ]

        if matches.empty:
            return None

        return matches.iloc[0]

    def get_recommendation(self, pest_name: str):

        pest_record = self.find_pest(pest_name)

        if pest_record is None:
            return {
                "status": "error",
                "message": f"Pest recommendation not found: {pest_name}"
            }

        return {
    "status": "success",
    "pest_id": pest_record["pest_id"],
    "pest_name": pest_record["pest_name"],
    "scientific_name": pest_record["scientific_name"],
    "pest_type": pest_record["pest_type"],
    "crops_affected": pest_record["crops_affected"],
    "description": pest_record["description"],
    "damage_symptoms": pest_record["damage_symptoms"],
    "damage_severity": pest_record["damage_severity"],
    "favorable_conditions": pest_record["favorable_conditions"],
    "organic_control": pest_record["organic_control"],
    "chemical_control": pest_record["chemical_control"],
    "prevention_measures": pest_record["prevention_measures"],
    "monitoring_actions": pest_record["monitoring_actions"]
}