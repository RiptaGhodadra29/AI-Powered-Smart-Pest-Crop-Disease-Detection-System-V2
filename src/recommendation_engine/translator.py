from deep_translator import GoogleTranslator


class RecommendationTranslator:

    def translate_text(
        self,
        text: str,
        target_language: str
    ):

        if not text:
            return text

        try:

            return GoogleTranslator(
                source="auto",
                target=target_language
            ).translate(text)

        except Exception:

            return text