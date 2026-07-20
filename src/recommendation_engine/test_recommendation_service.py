from src.recommendation_engine.recommendation_service import RecommendationService

service = RecommendationService()

print("\n=== Unknown Crop ===")
print(service.process_disease("Unknown_Crop"))

print("\n=== Healthy Crop ===")
print(service.process_disease("Tomato_healthy"))

print("\n=== New Disease ===")
print(service.process_disease("Mango Anthracnose"))