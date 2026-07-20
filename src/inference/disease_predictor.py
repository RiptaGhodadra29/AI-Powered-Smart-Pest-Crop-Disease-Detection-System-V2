import torch
import torch.nn.functional as F

from src.inference.image_preprocessor import preprocess_image
from src.inference.model_loader import load_disease_model
from src.inference.result_formatter import format_prediction_result


CLASS_NAMES = [
    "Apple_Rust",
    "Apple_Scab",
    "Apple_healthy",
    "Banana_Black_Sigatoka",
    "Banana_Bract_Mosaic_Virus",
    "Banana_Moko_Disease",
    "Banana_Panama_Disease",
    "Banana_Yellow_Sigatoka",
    "Banana_healthy",
    "Blueberry_healthy",
    "Cherry_healthy",
    "Corn_Blight",
    "Corn_Gray_Leaf_Spot",
    "Corn_Rust",
    "Grape_Black_Rot",
    "Grape_healthy",
    "Groundnut_Nutrition_Deficiency",
    "Groundnut_Rust",
    "Groundnut_Tikka_Leaf_Spot",
    "Groundnut_healthy",
    "Mango_Anthracnose",
    "Mango_Bacterial_Canker",
    "Mango_Cutting_Weevil",
    "Mango_Die_Back",
    "Mango_Gall_Midge",
    "Mango_Powdery_Mildew",
    "Mango_Sooty_Mould",
    "Mango_healthy",
    "Peach_healthy",
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry_healthy",
    "Rice_Bacterial_Blight",
    "Rice_Blast",
    "Rice_Brown_Spot",
    "Rice_Tungro",
    "Soybean_healthy",
    "Strawberry_healthy",
    "Sugarcane_Red_Rot",
    "Sugarcane_Rust",
    "Sugarcane_Smut",
    "Sugarcane_healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy",
    "Unknown_Crop",
    "Wheat_Brown_Rust",
    "Wheat_Powdery_Mildew",
    "Wheat_Yellow_Rust",
    "Wheat_healthy"
]


class DiseasePredictor:

    def __init__(self):

        self.model, self.device = load_disease_model()

    def predict(self, image_path):

        image = preprocess_image(image_path)

        image = image.to(self.device)

        self.model.eval()

        with torch.no_grad():

            outputs = self.model(image)

            probabilities = F.softmax(
                outputs,
                dim=1
            )

            confidence, predicted_class = torch.max(
                probabilities,
                dim=1
            )

        predicted_index = predicted_class.item()

        predicted_label = (
            CLASS_NAMES[predicted_index]
        )

        result = format_prediction_result(
            class_id=predicted_index,
            class_name=predicted_label,
            confidence=round(
                confidence.item() * 100,
                2
            ),
            prediction_type="disease",
            model_name="EfficientNet-B0"
        )

        return result