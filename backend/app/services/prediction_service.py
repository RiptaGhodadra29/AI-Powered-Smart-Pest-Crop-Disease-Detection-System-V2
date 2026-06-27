from backend.app.models.prediction import Prediction
from backend.app.models.uploaded_image import UploadedImage
from backend.app.models.recommendation import Recommendation

from backend.app.services.disease_predictor import (
    predict_disease
)

from backend.app.services.recommendation_service import (
    get_recommendation
)


def create_prediction(
    db,
    user_id,
    image_id
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

    # Run AI prediction
    result = predict_disease(
        image.image_path
    )

    # Get recommendation data
    recommendation = get_recommendation(
        result["class_name"]
    )

    # DEBUG PRINTS
    print("\n========================")
    print("CLASS =", result["class_name"])
    print("RECOMMENDATION =", recommendation)
    print("========================\n")

    # Create prediction record
    prediction = Prediction(
        user_id=user_id,
        image_id=image_id,
        prediction_type="disease",
        model_name=result["model_name"],
        class_id=result["class_id"],
        class_name=result["class_name"],
        confidence=result["confidence"]
    )

    # Save prediction
    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    # Create recommendation record
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

    # Save recommendation
    db.add(saved_recommendation)
    db.commit()
    db.refresh(saved_recommendation)

    # Confidence Score Calculation
    confidence = prediction.confidence

    if confidence >= 90:
        confidence_level = "High Confidence"
    elif confidence >= 70:
        confidence_level = "Medium Confidence"
    else:
        confidence_level = "Low Confidence"

    return {
        "prediction": prediction,
        "recommendation": recommendation,
        "confidence_level": confidence_level
    }