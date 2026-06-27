from pathlib import Path

import torch
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from src.models.efficientnet_b0 import EfficientNetB0
from src.data_preparation.dataset_loader import create_dataloaders


NUM_CLASSES = 34
BATCH_SIZE = 16


def main():

    if torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")

    print(f"\nUsing Device: {device}")

    dataset_root = (
        Path(__file__)
        .resolve()
        .parents[2]
        / "dataset"
        / "final_dataset_v2"
    )

    _, _, test_loader = create_dataloaders(
        dataset_root=dataset_root,
        batch_size=BATCH_SIZE
    )

    model = EfficientNetB0(
        num_classes=NUM_CLASSES,
        pretrained=False,
        freeze_features=False
    )

    model.load_state_dict(
        torch.load(
            "artifacts/models/best_model.pth",
            map_location=device
        )
    )

    model.to(device)
    model.eval()

    y_true = []
    y_pred = []

    with torch.no_grad():

        for images, labels in test_loader:

            images = images.to(device)

            outputs = model(images)

            _, preds = torch.max(outputs, 1)

            y_true.extend(labels.numpy())
            y_pred.extend(preds.cpu().numpy())

    accuracy = accuracy_score(
        y_true,
        y_pred
    )

    print("\nTest Accuracy")
    print("=" * 40)
    print(f"{accuracy * 100:.2f}%")

    print("\nClassification Report")
    print("=" * 40)

    class_names = (
        test_loader.dataset.dataset.classes
    )

    print(
        classification_report(
            y_true,
            y_pred,
            target_names=class_names
        )
    )

    print("\nConfusion Matrix")
    print("=" * 40)

    print(
        confusion_matrix(
            y_true,
            y_pred
        )
    )


if __name__ == "__main__":
    main()