import os
import json
import pandas as pd
from pathlib import Path

# ====================================================
# CONFIGURATION
# ====================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASETS = {
    "PlantVillage": PROJECT_ROOT / "dataset/raw/plantvillage",
    "PlantDoc": PROJECT_ROOT / "dataset/raw/plantdoc",
    "IP102": PROJECT_ROOT / "dataset/raw/ip102"
}

VALID_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
)

# ====================================================
# OUTPUT PATHS
# ====================================================

REPORT_DIR = PROJECT_ROOT / "dataset/reports/validation_report"
METADATA_DIR = PROJECT_ROOT / "dataset/metadata"

REPORT_DIR.mkdir(parents=True, exist_ok=True)
METADATA_DIR.mkdir(parents=True, exist_ok=True)

# ====================================================
# INVENTORY COLLECTION
# ====================================================

inventory_results = []

for dataset_name, dataset_path in DATASETS.items():

    print(f"\nChecking {dataset_name}...")

    if not dataset_path.exists():

        inventory_results.append({
            "dataset": dataset_name,
            "exists": False,
            "total_classes": 0,
            "total_images": 0,
            "empty_classes": 0
        })

        continue

    class_folders = [
        d for d in dataset_path.iterdir()
        if d.is_dir()
    ]

    total_images = 0
    empty_classes = 0

    for class_folder in class_folders:

        images = [
            f for f in class_folder.rglob("*")
            if f.suffix.lower() in VALID_EXTENSIONS
        ]

        total_images += len(images)

        if len(images) == 0:
            empty_classes += 1

    inventory_results.append({
        "dataset": dataset_name,
        "exists": True,
        "total_classes": len(class_folders),
        "total_images": total_images,
        "empty_classes": empty_classes
    })

# ====================================================
# SAVE REPORTS
# ====================================================

df = pd.DataFrame(inventory_results)

csv_report = REPORT_DIR / "dataset_inventory_report.csv"
df.to_csv(csv_report, index=False)

json_report = METADATA_DIR / "dataset_inventory.json"

with open(json_report, "w") as f:
    json.dump(inventory_results, f, indent=4)

print("\nInventory Verification Completed")
print(df)