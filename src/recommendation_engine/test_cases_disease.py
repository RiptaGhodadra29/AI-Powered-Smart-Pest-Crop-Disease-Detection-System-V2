from .recommendation_service import RecommendationService

service = RecommendationService()

test_diseases = [
    "Tomato Late Blight",
    "Tomato Early Blight",
    "Potato Early Blight",
    "Potato Late Blight",
    "Tomato Bacterial Spot"
]

for disease in test_diseases:

    print("\n" + "=" * 80)
    print(f"TESTING: {disease}")
    print("=" * 80)

    result = service.process_disease(
        disease
    )

    print(result)