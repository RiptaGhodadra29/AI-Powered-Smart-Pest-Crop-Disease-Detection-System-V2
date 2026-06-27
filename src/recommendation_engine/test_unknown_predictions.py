from .recommendation_service import RecommendationService

service = RecommendationService()

unknown_tests = [
    ("disease", "Banana Super Disease"),
    ("disease", "Random Disease"),
    ("pest", "Alien Insect"),
    ("pest", "Unknown Pest")
]

for prediction_type, prediction_name in unknown_tests:

    print("\n" + "=" * 80)
    print(f"TESTING: {prediction_type} -> {prediction_name}")
    print("=" * 80)

    result = service.process_prediction(
        prediction_type,
        prediction_name
    )

    print(result)