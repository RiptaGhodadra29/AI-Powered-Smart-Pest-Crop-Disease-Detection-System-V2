from .pest_recommender import PestRecommender
from .farmer_message_generator import FarmerMessageGenerator

recommender = PestRecommender()

generator = FarmerMessageGenerator()

recommendation = recommender.get_recommendation(
    "Caterpillars"
)

message = generator.generate_pest_message(
    recommendation
)

print(message)