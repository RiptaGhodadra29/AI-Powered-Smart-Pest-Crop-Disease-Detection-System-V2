from fastapi import APIRouter

from backend.app.services.gemini_service import GeminiService
from backend.app.services.disease_name_mapper import map_disease_name
from backend.app.services.recommendation_service import get_recommendation

router = APIRouter()

gemini_service = GeminiService()


@router.post("/regenerate")
def regenerate_recommendation(data: dict):

    disease_name = data.get("disease_name")
    language = data.get("language", "en")

    try:

        recommendation = (
            gemini_service.generate_disease_recommendation(
                disease_name,
                language
            )
        )

        recommendation["disease_name"] = disease_name

        recommendation["treatment"] = (
            "Refer to organic and chemical treatment."
        )

        return recommendation

    except Exception as e:

        print(
            f"\n❌ Gemini Regeneration Failed: {e}"
        )

        print(
            "\n🔄 Using CSV Fallback\n"
        )

        class_name = map_disease_name(
            disease_name
        )

        recommendation = get_recommendation(
            class_name,
            language
        )

        return recommendation