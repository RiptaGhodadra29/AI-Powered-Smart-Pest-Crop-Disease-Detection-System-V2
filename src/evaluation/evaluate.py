from pathlib import Path

import torch

from config.training_config import (
    BATCH_SIZE,
    NUM_CLASSES,
    MODEL_SAVE_PATH
)

from src.models.baseline_cnn import (
    BaselineCNN
)

from src.data_preparation.dataset_loader import (
    create_dataloaders
)

from src.training.utils import (
    get_device
)

from src.evaluation.evaluator import (
    Evaluator
)

from src.evaluation.metrics import (
    calculate_metrics,
    generate_classification_report,
    generate_confusion_matrix
)


def main():

    device = get_device()

    print(f"\nUsing Device: {device}")

    dataset_root = (
        Path(__file__)
        .resolve()
        .parents[2]
        / "dataset"
        / "final_dataset"
    )

    (
        _,
        _,
        test_loader
    ) = create_dataloaders(
        dataset_root=dataset_root,
        batch_size=BATCH_SIZE
    )

    model = BaselineCNN(
        num_classes=NUM_CLASSES
    )

    model.load_state_dict(
        torch.load(
            MODEL_SAVE_PATH,
            map_location=device
        )
    )

    evaluator = Evaluator(
        model=model,
        dataloader=test_loader,
        device=device
    )

    y_true, y_pred = evaluator.evaluate()

    metrics = calculate_metrics(
        y_true,
        y_pred
    )

    print("\nEvaluation Results")
    print("-" * 40)

    for metric, value in metrics.items():

        print(
            f"{metric}: {value:.4f}"
        )

    class_names = (
        test_loader.dataset.dataset.classes
    )

    print("\nClassification Report")
    print("-" * 40)

    print(
        generate_classification_report(
            y_true,
            y_pred,
            class_names
        )
    )

    print("\nConfusion Matrix")
    print("-" * 40)

    print(
        generate_confusion_matrix(
            y_true,
            y_pred
        )
    )


if __name__ == "__main__":
    main()