from pathlib import Path

import torch

from src.models.efficientnet_b0 import EfficientNetB0


MODEL_PATH = (
    Path(__file__)
    .resolve()
    .parents[2]
    / "artifacts"
    / "models"
    / "best_model.pth"
)


def get_device():
    """
    Select available device.
    """

    if torch.backends.mps.is_available():
        return torch.device("mps")

    if torch.cuda.is_available():
        return torch.device("cuda")

    return torch.device("cpu")


def load_disease_model():
    """
    Load trained EfficientNet-B0 model.
    """

    device = get_device()

    model = EfficientNetB0(
        num_classes=60,
        pretrained=False,
        freeze_features=False
    )

    model.load_state_dict(
        torch.load(
            MODEL_PATH,
            map_location=device
        )
    )

    model.to(device)

    model.eval()

    return model, device