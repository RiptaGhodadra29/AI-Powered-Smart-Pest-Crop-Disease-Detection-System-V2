import json
from pathlib import Path

import matplotlib.pyplot as plt


def plot_training_curves():

    history_path = (
        Path(__file__)
        .resolve()
        .parents[2]
        / "artifacts"
        / "history"
        / "training_history.json"
    )

    with open(history_path, "r") as file:
        history = json.load(file)

    train_losses = history["train_losses"]
    val_losses = history["val_losses"]

    train_accs = history["train_accuracies"]
    val_accs = history["val_accuracies"]

    plots_dir = (
        Path(__file__)
        .resolve()
        .parents[2]
        / "artifacts"
        / "plots"
    )

    plots_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    # Loss Curve

    plt.figure(figsize=(8, 5))

    plt.plot(
        train_losses,
        label="Train Loss"
    )

    plt.plot(
        val_losses,
        label="Validation Loss"
    )

    plt.title("Loss Curve")

    plt.xlabel("Epoch")

    plt.ylabel("Loss")

    plt.legend()

    plt.grid(True)

    plt.savefig(
        plots_dir / "loss_curve.png"
    )

    plt.close()

    # Accuracy Curve

    plt.figure(figsize=(8, 5))

    plt.plot(
        train_accs,
        label="Train Accuracy"
    )

    plt.plot(
        val_accs,
        label="Validation Accuracy"
    )

    plt.title("Accuracy Curve")

    plt.xlabel("Epoch")

    plt.ylabel("Accuracy (%)")

    plt.legend()

    plt.grid(True)

    plt.savefig(
        plots_dir / "accuracy_curve.png"
    )

    plt.close()

    print(
        "\nTraining Curves Saved Successfully"
    )


if __name__ == "__main__":
    plot_training_curves()