from .recommendation_service import RecommendationService

service = RecommendationService()

result = service.process_prediction(
    "disease",
    "Tomato Late Blight"
)

print(result)