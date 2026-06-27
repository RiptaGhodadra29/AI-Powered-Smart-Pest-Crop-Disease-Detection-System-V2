from .prediction_recommendation_pipeline import (
    PredictionRecommendationPipeline
)

pipeline = PredictionRecommendationPipeline()

print("\nDisease Test")

print(
    pipeline.get_disease_recommendation(
        "Tomato_Late_blight"
    )
)

print("\nHealthy Test")

print(
    pipeline.get_disease_recommendation(
        "Tomato_healthy"
    )
)

print("\nUnknown Test")

print(
    pipeline.get_disease_recommendation(
        "Unknown_Crop"
    )
)