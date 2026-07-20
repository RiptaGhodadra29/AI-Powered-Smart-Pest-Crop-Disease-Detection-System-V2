import json
from pathlib import Path


class TranslationLoader:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.translation_path = (
            self.project_root
            / "recommendation_engine"
            / "translations"
        )

    def load_translation(
        self,
        category: str,
        language: str
    ):

        file_path = (
            self.translation_path
            / f"{category}_{language}.json"
        )

        if not file_path.exists():
            return {}

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except Exception:

            return {}