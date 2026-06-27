from src.pest_detection.pest_recommendation_pipeline import (
    PestRecommendationPipeline
)

IMAGE_PATH = "/Users/ripta/Desktop/AI_Powered_Smart_Pest_Crop_Disease_Detection_System/dataset/raw/agripest/test/images/grasshopper-11-_jpg.rf.0746dc023efddc064bcdd4c2784fbf16.jpg"

pipeline = PestRecommendationPipeline()

result = pipeline.process_image(
    IMAGE_PATH
)

print(result)