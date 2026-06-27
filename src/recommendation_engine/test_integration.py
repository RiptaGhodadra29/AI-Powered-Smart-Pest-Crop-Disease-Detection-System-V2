from .recommendation_service import RecommendationService

service = RecommendationService()

integration_tests = [
    ("disease", "Tomato Late Blight"),
    ("disease", "Potato Early Blight"),
    ("pest", "Caterpillars"),
    ("pest", "Grasshoppers")
]

for prediction_type, prediction_name in integration_tests:

    print("\n" + "=" * 80)
    print(f"PIPELINE TEST: {prediction_type} -> {prediction_name}")
    print("=" * 80)

    result = service.process_prediction(
        prediction_type,
        prediction_name
    )

    print(result)