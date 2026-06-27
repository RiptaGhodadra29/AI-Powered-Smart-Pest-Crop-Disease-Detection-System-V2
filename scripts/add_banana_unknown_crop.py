import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

SOURCE_ROOT = Path(
    "/Users/ripta/Downloads/banana_leaf_dataset"
)

TARGET_ROOT = Path(
    "dataset/final_dataset_v2"
)

all_images = []

for folder in ["Healthy", "Unhealthy"]:

    source_dir = SOURCE_ROOT / folder

    for ext in ["*.jpg", "*.jpeg", "*.png", "*.JPG"]:
        all_images.extend(
            list(source_dir.glob(ext))
        )

print(
    f"Total Banana Images: {len(all_images)}"
)

train_imgs, temp_imgs = train_test_split(
    all_images,
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
        "Unknown_Crop"
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
    "\n✓ Banana images added to Unknown_Crop"
)