from src.inference.disease_predictor import DiseasePredictor


IMAGE_PATH = (
    "dataset/final_dataset/test/"
    "Tomato_healthy/"
    "efe6c986-b85c-40f1-8cb5-345acbb36b71___RS_HL 0579.JPG"
)


predictor = DiseasePredictor()

result = predictor.predict(
    IMAGE_PATH
)

print("\nPrediction Result")
print(result)