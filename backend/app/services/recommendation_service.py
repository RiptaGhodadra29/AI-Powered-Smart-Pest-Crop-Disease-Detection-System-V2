from src.recommendation_engine.disease_recommender import (
    DiseaseRecommender
)

from src.recommendation_engine.pest_recommender import (
    PestRecommender
)

from backend.app.services.disease_name_mapper import (
    map_disease_name
)


disease_recommender = DiseaseRecommender()
pest_recommender = PestRecommender()


def get_recommendation(
    class_name: str
):

    mapped_name = map_disease_name(
        class_name
    )

    recommendation = (
        disease_recommender.get_recommendation(
            mapped_name
        )
    )

    if recommendation["status"] != "success":

        return {
            "disease_name": mapped_name,
            "severity": "Unknown",
            "description": "Recommendation not available",
            "treatment": "Consult agricultural expert",
            "organic_treatment": "",
            "chemical_treatment": "",
            "preventive_measures": "",
            "monitoring_actions": ""
        }

    return {
        "disease_name": recommendation["disease_name"],
        "severity": recommendation["severity_level"],
        "description": recommendation["description"],
        "treatment": recommendation["treatment"],
        "organic_treatment": recommendation["organic_treatment"],
        "chemical_treatment": recommendation["chemical_treatment"],
        "preventive_measures": recommendation["preventive_measures"],
        "monitoring_actions": recommendation["monitoring_actions"]
    }


def get_pest_recommendation(
    pest_name: str
):

    recommendation = (
        pest_recommender.get_recommendation(
            pest_name
        )
    )

    if recommendation["status"] != "success":

        return {
            "pest_name": pest_name,
            "damage_severity": "Unknown",
            "description": "Recommendation not available",
            "organic_control": "",
            "chemical_control": "",
            "prevention_measures": "",
            "monitoring_actions": ""
        }

    return recommendation