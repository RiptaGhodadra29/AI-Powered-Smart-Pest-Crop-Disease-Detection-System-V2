from .recommendation_service import RecommendationService

service = RecommendationService()

test_cases = [
    ("disease", ""),
    ("disease", "   "),
    ("disease", "tomato late blight"),
    ("disease", "TOMATO LATE BLIGHT"),
    ("pest", ""),
    ("pest", "   "),
    ("pest", "caterpillars"),
    ("pest", "CATERPILLARS"),
    ("weather", "rain"),
]

for prediction_type, prediction_name in test_cases:

    print("\n" + "=" * 80)
    print(f"TYPE: {prediction_type}")
    print(f"INPUT: {prediction_name}")
    print("=" * 80)

    result = service.process_prediction(
        prediction_type,
        prediction_name
    )

    print(result)