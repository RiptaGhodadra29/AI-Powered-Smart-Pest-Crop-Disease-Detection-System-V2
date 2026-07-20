from pathlib import Path

from src.inference.disease_predictor import DiseasePredictor

predictor = DiseasePredictor()

extensions = [
    "*.jpg",
    "*.jpeg",
    "*.png",
    "*.webp"
]

dataset_root = Path("unknown_datasets")

for dataset in dataset_root.iterdir():

    if not dataset.is_dir():
        continue

    print("\n" + "=" * 60)
    print(dataset.name)
    print("=" * 60)

    images = []

    for ext in extensions:
        images.extend(
            dataset.rglob(ext)
        )

    print(f"Found {len(images)} images")

    unknown_count = 0

    for image_path in images[:100]:

        result = predictor.predict(
            str(image_path)
        )

        predicted = result["class_name"]

        if predicted == "Unknown_Crop":
            unknown_count += 1

        print(
            f"{image_path.name} -> "
            f"{predicted} "
            f"({result['confidence']}%)"
        )

    print(
        f"\nUnknown Predictions: "
        f"{unknown_count}/{min(100,len(images))}"
    )