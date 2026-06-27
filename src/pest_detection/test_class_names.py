from src.pest_detection.model_loader import (
    load_pest_model
)

model = load_pest_model()

print(model.names)