from backend.app.models.prediction import Prediction
from backend.app.models.uploaded_image import UploadedImage
from backend.app.models.recommendation import Recommendation

from backend.app.services.disease_predictor import (
    predict_disease
)

from backend.app.services.gemini_service import (
    GeminiService
)

from backend.app.services.recommendation_service import (
    get_recommendation
)

from backend.app.services.disease_name_mapper import (
    map_disease_name
)

gemini_service = GeminiService()


def create_prediction(
    db,
    user_id,
    image_id,
    language="en"
):

    image = (
        db.query(UploadedImage)
        .filter(
            UploadedImage.id == image_id
        )
        .first()
    )

    if not image:
        return None

    # ==================================================
    # Disease Prediction
    # ==================================================

    result = predict_disease(
        image.image_path
    )

    # ==================================================
    # Unknown Crop Handling
    # ==================================================

    if result["class_name"] == "Unknown_Crop":

        recommendation = {
            "disease_name": "Unknown Crop",

            "severity": "Not Applicable",

            "description":
                "The uploaded image does not belong to any crop currently supported by this system.",

            "treatment":
                "No treatment recommendation available because crop identification failed.",

            "organic_treatment": [
                "Upload a clearer leaf image.",
                "Capture only one leaf.",
                "Use natural daylight.",
                "Avoid blurry images."
            ],

            "chemical_treatment": [
                "Not applicable until crop is identified."
            ],

            "preventive_measures": [
                "Verify crop type before diagnosis.",
                "Ensure leaf is fully visible.",
                "Retake image from closer distance."
            ],

            "monitoring_actions": [
                "Try another image.",
                "Consult agricultural expert if symptoms persist."
            ]
        }

    else:

        # ==================================================
        # Map Disease Name
        # ==================================================

        mapped_name = map_disease_name(
            result["class_name"]
        )

        # ==================================================
        # Gemini Recommendation (Primary)
        # CSV Recommendation (Fallback)
        # ==================================================

        try:

            recommendation = (
                gemini_service.generate_disease_recommendation(
                    mapped_name,
                    language
                )
            )

            recommendation["treatment"] = (
                "Refer to organic and chemical treatment."
            )

            print(
                f"\n✅ Gemini Recommendation Used for: {mapped_name}\n"
            )

        except Exception as e:

            print(
                f"\n❌ Gemini Failed: {e}"
            )

            print(
                f"🔄 Falling back to CSV Recommendation Engine...\n"
            )

            recommendation = get_recommendation(
                result["class_name"],
                language
            )

    # ==================================================
    # DEBUG
    # ==================================================

    print("\n========================")
    print("CLASS =", result["class_name"])
    print("LANGUAGE =", language)
    print("RECOMMENDATION =", recommendation)
    print("========================\n")

    # ==================================================
    # Save Prediction
    # ==================================================

    prediction = Prediction(
        user_id=user_id,
        image_id=image_id,
        prediction_type="disease",
        model_name=result["model_name"],
        class_id=result["class_id"],
        class_name=result["class_name"],
        confidence=result["confidence"]
    )

    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    # ==================================================
    # Save Recommendation
    # ==================================================

    saved_recommendation = Recommendation(
        prediction_id=prediction.id,
        disease_name=recommendation["disease_name"],
        severity=recommendation["severity"],
        description=recommendation["description"],
        treatment=recommendation["treatment"],
        organic_treatment=str(
            recommendation["organic_treatment"]
        ),
        chemical_treatment=str(
            recommendation["chemical_treatment"]
        ),
        preventive_measures=str(
            recommendation["preventive_measures"]
        ),
        monitoring_actions=str(
            recommendation["monitoring_actions"]
        )
    )

    db.add(saved_recommendation)
    db.commit()
    db.refresh(saved_recommendation)

    # ==================================================
    # Confidence Level
    # ==================================================

    confidence = prediction.confidence

    if confidence >= 90:

        confidence_level = (
            "High Confidence"
        )

    elif confidence >= 70:

        confidence_level = (
            "Medium Confidence"
        )

    else:

        confidence_level = (
            "Low Confidence"
        )

    # ==================================================
    # Response
    # ==================================================

    return {
        "prediction": prediction,
        "recommendation": recommendation,
        "confidence_level": confidence_level
    }