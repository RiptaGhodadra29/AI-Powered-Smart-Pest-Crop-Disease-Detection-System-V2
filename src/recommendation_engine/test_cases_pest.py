from .recommendation_service import RecommendationService

service = RecommendationService()

test_pests = [
    "Ants",
    "Beetles",
    "Caterpillars",
    "Grasshoppers",
    "Weevils"
]

for pest in test_pests:

    print("\n" + "=" * 80)
    print(f"TESTING: {pest}")
    print("=" * 80)

    result = service.process_pest(
        pest
    )

    print(result)