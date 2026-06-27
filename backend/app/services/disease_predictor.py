from src.inference.unified_predictor import (
    UnifiedPredictor
)

predictor = UnifiedPredictor()


def predict_disease(
    image_path: str
):

    result = predictor.predict_disease(
        image_path
    )

    return {
        "class_id": result["class_id"],
        "class_name": result["class_name"],
        "confidence": result["confidence"],
        "model_name": result["model_name"]
    }