import json
from pathlib import Path

from config.training_config import (
    BATCH_SIZE,
    EPOCHS,
    LEARNING_RATE,
    MODEL_SAVE_PATH,
    SEED,
    NUM_CLASSES
)

from src.data_preparation.dataset_loader import (
    create_dataloaders
)

from src.models.baseline_cnn import (
    BaselineCNN
)

from src.training.loss_optimizer import (
    get_loss_function,
    get_optimizer
)

from src.training.trainer import (
    Trainer
)

from src.training.utils import (
    set_seed,
    get_device,
    save_model
)


def main():

    set_seed(SEED)

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
        train_loader,
        validation_loader,
        _
    ) = create_dataloaders(
        dataset_root=dataset_root,
        batch_size=BATCH_SIZE
    )

    model = BaselineCNN(
        num_classes=NUM_CLASSES
    )

    criterion = get_loss_function()

    optimizer = get_optimizer(
        model,
        learning_rate=LEARNING_RATE
    )

    trainer = Trainer(
        model=model,
        criterion=criterion,
        optimizer=optimizer,
        device=device
    )

    best_val_loss = float("inf")

    # Training History
    train_losses = []
    val_losses = []

    train_accuracies = []
    val_accuracies = []

    for epoch in range(EPOCHS):

        train_loss, train_acc = (
            trainer.train_one_epoch(
                train_loader
            )
        )

        val_loss, val_acc = (
            trainer.validate(
                validation_loader
            )
        )

        # Save history
        train_losses.append(train_loss)
        val_losses.append(val_loss)

        train_accuracies.append(train_acc)
        val_accuracies.append(val_acc)

        print(
            f"\nEpoch [{epoch+1}/{EPOCHS}]"
        )

        print(
            f"Train Loss: {train_loss:.4f} | "
            f"Train Acc: {train_acc:.2f}%"
        )

        print(
            f"Val Loss: {val_loss:.4f} | "
            f"Val Acc: {val_acc:.2f}%"
        )

        if val_loss < best_val_loss:

            best_val_loss = val_loss

            save_model(
                model,
                MODEL_SAVE_PATH
            )

            print(
                "Best model updated."
            )

    history = {
        "train_losses": train_losses,
        "val_losses": val_losses,
        "train_accuracies": train_accuracies,
        "val_accuracies": val_accuracies
    }

    print("\nTraining Complete")

    history_dir = (
        Path(__file__)
        .resolve()
        .parents[2]
        / "artifacts"
        / "history"
    )

    history_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    history_file = (
        history_dir
        / "training_history.json"
    )

    with open(
        history_file,
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )

    print(
        f"\nTraining History Saved: "
        f"{history_file}"
    )

    return history


if __name__ == "__main__":
    main()