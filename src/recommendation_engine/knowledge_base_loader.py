"""
Knowledge Base Loader

Loads:
1. Disease Knowledge Base
2. Pest Knowledge Base

Author: AI-Powered Smart Pest & Crop Disease Detection System
"""

from pathlib import Path
import pandas as pd


class KnowledgeBaseLoader:
    """
    Loads recommendation knowledge base files.
    """

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.disease_kb_path = (
            self.project_root
            / "recommendation_engine"
            / "disease_knowledge_base.csv"
        )

        self.pest_kb_path = (
            self.project_root
            / "recommendation_engine"
            / "pest_knowledge_base.csv"
        )

    def load_disease_kb(self) -> pd.DataFrame:
        """
        Load disease knowledge base.
        """

        return pd.read_csv(self.disease_kb_path)

    def load_pest_kb(self) -> pd.DataFrame:
        """
        Load pest knowledge base.
        """

        return pd.read_csv(self.pest_kb_path)

    def load_all(self):
        """
        Load both knowledge bases.
        """

        disease_df = self.load_disease_kb()
        pest_df = self.load_pest_kb()

        return disease_df, pest_df