from pathlib import Path
import shutil
import random

random.seed(42)

SOURCE = Path("dataset/final_dataset_v2/train")

VAL_DIR = Path("dataset/final_dataset_v2/val")
TEST_DIR = Path("dataset/final_dataset_v2/test")

VAL_DIR.mkdir(parents=True, exist_ok=True)
TEST_DIR.mkdir(parents=True, exist_ok=True)

for class_dir in SOURCE.iterdir():

    if not class_dir.is_dir():
        continue

    images = []

    for ext in ["*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"]:
        images.extend(class_dir.glob(ext))

    random.shuffle(images)

    total = len(images)

    val_count = int(total * 0.15)
    test_count = int(total * 0.15)

    val_images = images[:val_count]
    test_images = images[val_count:val_count + test_count]

    (VAL_DIR / class_dir.name).mkdir(parents=True, exist_ok=True)
    (TEST_DIR / class_dir.name).mkdir(parents=True, exist_ok=True)

    for img in val_images:
        shutil.copy2(
            img,
            VAL_DIR / class_dir.name / img.name
        )

    for img in test_images:
        shutil.copy2(
            img,
            TEST_DIR / class_dir.name / img.name
        )

print("Dataset Split Complete")