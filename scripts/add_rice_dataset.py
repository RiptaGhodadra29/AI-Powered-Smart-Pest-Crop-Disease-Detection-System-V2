import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

SOURCE_ROOT = Path(
    "/Users/ripta/Downloads/Rice Leaf Disease Images"
)

TARGET_ROOT = Path(
    "dataset/final_dataset_v2"
)

CLASS_MAPPING = {
    "Bacterialblight": "Rice_Bacterial_Blight",
    "Blast": "Rice_Blast",
    "Brownspot": "Rice_Brown_Spot",
    "Tungro": "Rice_Tungro"
}

for source_class, target_class in CLASS_MAPPING.items():

    source_dir = SOURCE_ROOT / source_class

    images = []

    for ext in ["*.jpg", "*.jpeg", "*.png", "*.JPG"]:
        images.extend(
            list(source_dir.glob(ext))
        )

    train_imgs, temp_imgs = train_test_split(
        images,
        test_size=0.20,
        random_state=42
    )

    val_imgs, test_imgs = train_test_split(
        temp_imgs,
        test_size=0.50,
        random_state=42
    )

    splits = {
        "train": train_imgs,
        "validation": val_imgs,
        "test": test_imgs
    }

    for split_name, split_images in splits.items():

        target_dir = (
            TARGET_ROOT /
            split_name /
            target_class
        )

        target_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        for img in split_images:
            shutil.copy(
                img,
                target_dir / img.name
            )

    print(
        f"✓ {target_class} integrated"
    )

print(
    "\nRice dataset integrated successfully."
)