from .pest_recommender import PestRecommender

recommender = PestRecommender()

result = recommender.get_recommendation(
    "Caterpillars"
)

print(result)