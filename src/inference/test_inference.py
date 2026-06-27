from src.inference.model_loader import (
    load_disease_model
)


def main():

    model, device = load_disease_model()

    print("\nModel Loaded Successfully")

    print(f"Device: {device}")

    print(type(model).__name__)


if __name__ == "__main__":
    main()