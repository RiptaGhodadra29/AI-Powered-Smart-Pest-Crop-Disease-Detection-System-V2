import shutil
from pathlib import Path

mappings = {
    "Apple leaf": "Apple_healthy",
    "Apple Scab Leaf": "Apple_Scab",
    "Apple rust leaf": "Apple_Rust",

    "Corn leaf blight": "Corn_Blight",
    "Corn Gray leaf spot": "Corn_Gray_Leaf_Spot",
    "Corn rust leaf": "Corn_Rust",

    "grape leaf": "Grape_healthy",
    "grape leaf black rot": "Grape_Black_Rot",

    "Blueberry leaf": "Blueberry_healthy",
    "Cherry leaf": "Cherry_healthy",
    "Peach leaf": "Peach_healthy",
    "Raspberry leaf": "Raspberry_healthy",
    "Soyabean leaf": "Soybean_healthy",
    "Strawberry leaf": "Strawberry_healthy",
}

base_source = Path("dataset/processed/plantdoc")
base_target = Path("dataset/final_dataset_v2")

for source_name, target_name in mappings.items():

    train_source = base_source / "train" / source_name
    test_source = base_source / "test" / source_name

    train_target = base_target / "train" / target_name
    validation_target = base_target / "validation" / target_name
    test_target = base_target / "test" / target_name

    train_images = list(train_source.glob("*"))
    test_images = list(test_source.glob("*"))

    # 80% train
    split_index = int(len(train_images) * 0.8)

    train_part = train_images[:split_index]
    validation_part = train_images[split_index:]

    for img in train_part:
        shutil.copy(img, train_target)

    for img in validation_part:
        shutil.copy(img, validation_target)

    for img in test_images:
        shutil.copy(img, test_target)

    print(f"✓ {target_name} copied")

print("\nDataset V2 updated successfully.")