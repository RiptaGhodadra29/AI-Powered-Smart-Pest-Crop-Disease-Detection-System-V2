class FarmerResponseService:

    @staticmethod
    def format_disease_response(result):

        prediction = result["prediction"]
        recommendation = result["recommendation"]

        return {
            "prediction_type": "disease",
            "prediction_name": prediction.class_name,
            "confidence": prediction.confidence,
            "confidence_level": result["confidence_level"],
            "model_name": prediction.model_name,
            "recommendation": recommendation
        }

    @staticmethod
    def format_pest_response(result):

        if len(result) == 0:

            return {
                "prediction_type": "pest",
                "message": "No pest detected"
            }

        pest = result[0]

        confidence = pest["confidence"]

        if confidence >= 90:
            confidence_level = "High Confidence"
        elif confidence >= 70:
            confidence_level = "Medium Confidence"
        else:
            confidence_level = "Low Confidence"

        return {
            "prediction_type": "pest",
            "prediction_name": pest["pest_name"],
            "confidence": pest["confidence"],
            "confidence_level": confidence_level,
            "recommendation": pest["recommendation"]
        }