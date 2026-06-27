def format_prediction_result(
    class_id,
    class_name,
    confidence,
    prediction_type="disease",
    model_name="EfficientNet-B0"
):
    """
    Format prediction output into a
    standardized structure.
    """

    return {
        "status": "success",
        "prediction_type": prediction_type,
        "model_name": model_name,
        "class_id": class_id,
        "class_name": class_name,
        "confidence": confidence
    }