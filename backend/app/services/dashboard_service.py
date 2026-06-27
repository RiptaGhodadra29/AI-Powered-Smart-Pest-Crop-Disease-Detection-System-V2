from collections import Counter

from backend.app.models.prediction import Prediction


def get_dashboard_data(
    db,
    user_id
):

    predictions = (
        db.query(Prediction)
        .filter(
            Prediction.user_id == user_id
        )
        .all()
    )

    if not predictions:
        return {
            "user_id": user_id,
            "total_predictions": 0,
            "most_detected_disease": "None",
            "average_confidence": 0.0
        }

    total_predictions = len(predictions)

    disease_names = [
        prediction.class_name
        for prediction in predictions
    ]

    most_detected_disease = (
        Counter(disease_names)
        .most_common(1)[0][0]
    )

    average_confidence = round(
        sum(
            prediction.confidence
            for prediction in predictions
        ) / total_predictions,
        2
    )

    return {
        "user_id": user_id,
        "total_predictions": total_predictions,
        "most_detected_disease": most_detected_disease,
        "average_confidence": average_confidence
    }