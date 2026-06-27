from src.inference.predict_and_recommend import (
    PredictAndRecommend
)

IMAGE_PATH = (
    "dataset/final_dataset/test/"
    "Tomato_healthy/"
    "efe6c986-b85c-40f1-8cb5-345acbb36b71___RS_HL 0579.JPG"
)

service = PredictAndRecommend()

result = service.process_image(
    IMAGE_PATH
)

print(result)