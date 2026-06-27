from .model_loader import load_pest_model


class PestPredictor:

    def __init__(self):
        self.model = load_pest_model()

    def predict(self, image_path):

        results = self.model(image_path)

        if len(results[0].boxes) == 0:
            return None

        box = results[0].boxes[0]

        class_id = int(box.cls.item())

        confidence = float(box.conf.item())

        pest_name = self.model.names[class_id]

        return {
            "pest_name": pest_name,
            "confidence": round(confidence * 100, 2)
        }