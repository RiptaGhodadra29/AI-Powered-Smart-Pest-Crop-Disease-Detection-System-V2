import os
import random
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps

DATASET_DIR = "dataset/final_dataset_v2/train"

TARGET_COUNT = 300

SMALL_CLASSES = [
    "Corn_Blight",
    "Corn_Rust",
    "Potato___healthy",
    "Tomato__Tomato_mosaic_virus"
]


def augment_image(image):

    operations = [
        lambda img: img.rotate(
            random.randint(-25, 25)
        ),

        lambda img: ImageOps.mirror(img),

        lambda img: ImageOps.flip(img),

        lambda img: ImageEnhance.Brightness(
            img
        ).enhance(
            random.uniform(0.8, 1.2)
        ),

        lambda img: ImageEnhance.Contrast(
            img
        ).enhance(
            random.uniform(0.8, 1.2)
        ),
    ]

    operation = random.choice(
        operations
    )

    return operation(image)


for class_name in SMALL_CLASSES:

    class_dir = os.path.join(
        DATASET_DIR,
        class_name
    )

    images = [
        f for f in os.listdir(class_dir)
        if f.lower().endswith(
            (".jpg", ".jpeg", ".png")
        )
    ]

    current_count = len(images)

    print(
        f"\n{class_name}: "
        f"{current_count} images"
    )

    if current_count >= TARGET_COUNT:
        continue

    needed = (
        TARGET_COUNT -
        current_count
    )

    print(
        f"Generating "
        f"{needed} images..."
    )

    for i in range(needed):

        img_name = random.choice(
            images
        )

        img_path = os.path.join(
            class_dir,
            img_name
        )

        image = Image.open(
            img_path
        ).convert("RGB")

        augmented = augment_image(
            image
        )

        save_name = (
            f"aug_{i}_"
            f"{img_name}"
        )

        save_path = os.path.join(
            class_dir,
            save_name
        )

        augmented.save(
            save_path
        )

    print(
        f"✓ {class_name} balanced"
    )

print(
    "\nDataset balancing completed."
)