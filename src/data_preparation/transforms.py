from albumentations import (
    Compose,
    Resize,
    HorizontalFlip,
    Rotate,
    RandomBrightnessContrast,
    Normalize
)

from albumentations.pytorch import ToTensorV2


IMAGE_SIZE = 224


def get_train_transforms():
    """
    Training transforms with augmentation.
    """

    return Compose([
        Resize(
            height=IMAGE_SIZE,
            width=IMAGE_SIZE
        ),

        HorizontalFlip(
            p=0.5
        ),

        Rotate(
            limit=15,
            p=0.5
        ),

        RandomBrightnessContrast(
            p=0.5
        ),

        Normalize(),

        ToTensorV2()
    ])


def get_validation_transforms():
    """
    Validation transforms.
    """

    return Compose([
        Resize(
            height=IMAGE_SIZE,
            width=IMAGE_SIZE
        ),

        Normalize(),

        ToTensorV2()
    ])


def get_test_transforms():
    """
    Test transforms.
    """

    return Compose([
        Resize(
            height=IMAGE_SIZE,
            width=IMAGE_SIZE
        ),

        Normalize(),

        ToTensorV2()
    ])