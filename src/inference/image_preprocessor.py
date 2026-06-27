from PIL import Image
import numpy as np

from albumentations import (
    Compose,
    Resize,
    Normalize
)

from albumentations.pytorch import ToTensorV2


IMAGE_SIZE = 224


def get_inference_transform():
    """
    Preprocessing pipeline for inference.
    """

    return Compose([
        Resize(
            height=IMAGE_SIZE,
            width=IMAGE_SIZE
        ),
        Normalize(),
        ToTensorV2()
    ])


def preprocess_image(image_path):
    """
    Load and preprocess image.
    """

    image = Image.open(image_path)

    image = image.convert("RGB")

    image = np.array(image)

    transform = get_inference_transform()

    image = transform(
        image=image
    )["image"]

    image = image.unsqueeze(0)

    return image