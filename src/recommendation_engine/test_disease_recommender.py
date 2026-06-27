from .disease_recommender import DiseaseRecommender

recommender = DiseaseRecommender()

result = recommender.get_recommendation(
    "Tomato Late Blight"
)

print(result)
