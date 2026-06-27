from src.inference.unified_predictor import (
    UnifiedPredictor
)

IMAGE_PATH = (
    "dataset/final_dataset/test/"
    "Tomato_healthy/"
    "efe6c986-b85c-40f1-8cb5-345acbb36b71___RS_HL 0579.JPG"
)

predictor = UnifiedPredictor()

result = predictor.predict_disease(
    IMAGE_PATH
)

print("\nUnified Predictor Result")
print(result)