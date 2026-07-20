import pandas as pd

from backend.app.services.disease_name_mapper import (
    map_disease_name
)

CSV_PATH = (
    "recommendation_engine/"
    "disease_knowledge_base.csv"
)


def get_recommendation(
    disease_name: str,
    language: str = "en"
):

    try:

        mapped_name = map_disease_name(
            disease_name
        )

        df = pd.read_csv(
            CSV_PATH
        )

        disease_row = df[
            df["disease_name"]
            .str.lower()
            ==
            mapped_name.lower()
        ]

        if disease_row.empty:

            return {
                "disease_name": mapped_name,
                "severity": "Unknown",
                "description":
                    f"No recommendation found for {mapped_name}",
                "treatment":
                    "Consult agricultural expert.",
                "organic_treatment":
                    "Not Available",
                "chemical_treatment":
                    "Not Available",
                "preventive_measures":
                    "Not Available",
                "monitoring_actions":
                    "Monitor crop condition"
            }

        disease_row = disease_row.iloc[0]

        return {

            "disease_name":
                disease_row["disease_name"],

            "severity":
                disease_row["severity_level"],

            "description":
                disease_row["description"],

            "treatment":
                disease_row["treatment"],

            "organic_treatment":
                disease_row["organic_treatment"],

            "chemical_treatment":
                disease_row["chemical_treatment"],

            "preventive_measures":
                disease_row["preventive_measures"],

            "monitoring_actions":
                disease_row["monitoring_actions"]
        }

    except Exception as e:

        print(
            f"CSV Recommendation Error: {e}"
        )

        return {
            "disease_name": disease_name,
            "severity": "Unknown",
            "description":
                "Recommendation currently unavailable.",
            "treatment":
                "Not Available",
            "organic_treatment":
                "Not Available",
            "chemical_treatment":
                "Not Available",
            "preventive_measures":
                "Not Available",
            "monitoring_actions":
                "Not Available"
        }