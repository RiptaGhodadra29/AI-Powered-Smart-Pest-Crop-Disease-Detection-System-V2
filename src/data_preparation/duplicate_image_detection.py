from pathlib import Path
import hashlib
import pandas as pd
import json
from datetime import datetime

# ==================================================
# CONFIG
# ==================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET_ROOT = PROJECT_ROOT / "dataset/raw"

REPORT_DIR = (
    PROJECT_ROOT /
    "dataset/reports/preprocessing_report"
)

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

VALID_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
)

# ==================================================
# HASH FUNCTION
# ==================================================

def calculate_md5(file_path):

    md5 = hashlib.md5()

    with open(file_path, "rb") as f:

        while chunk := f.read(8192):
            md5.update(chunk)

    return md5.hexdigest()

# ==================================================
# COLLECT IMAGES
# ==================================================

all_images = [
    file
    for file in DATASET_ROOT.rglob("*")
    if file.suffix.lower() in VALID_EXTENSIONS
]

print(f"\nTotal Images Found: {len(all_images)}")

# ==================================================
# DUPLICATE DETECTION
# ==================================================

hash_map = {}

for idx, image_path in enumerate(all_images, start=1):

    if idx % 5000 == 0:
        print(
            f"Processed {idx}/{len(all_images)}"
        )

    file_hash = calculate_md5(image_path)

    hash_map.setdefault(
        file_hash,
        []
    ).append(str(image_path))

# ==================================================
# FIND DUPLICATES
# ==================================================

duplicate_records = []

duplicate_groups = 0
duplicate_images = 0

for file_hash, files in hash_map.items():

    if len(files) > 1:

        duplicate_groups += 1
        duplicate_images += len(files)

        for file_path in files:

            duplicate_records.append({
                "hash": file_hash,
                "image_path": file_path,
                "group_size": len(files)
            })

# ==================================================
# SAVE CSV REPORT
# ==================================================

duplicate_df = pd.DataFrame(
    duplicate_records
)

csv_path = (
    REPORT_DIR /
    "duplicate_image_report.csv"
)

duplicate_df.to_csv(
    csv_path,
    index=False
)

# ==================================================
# SAVE SUMMARY
# ==================================================

duplicate_percentage = round(
    (duplicate_images / len(all_images)) * 100,
    4
)

summary = {
    "scan_date": str(datetime.now()),
    "total_images_scanned": len(all_images),
    "duplicate_groups": duplicate_groups,
    "duplicate_images": duplicate_images,
    "duplicate_percentage": duplicate_percentage
}

json_path = (
    REPORT_DIR /
    "duplicate_summary.json"
)

with open(json_path, "w") as f:
    json.dump(summary, f, indent=4)

# ==================================================
# FINAL OUTPUT
# ==================================================

print("\nDuplicate Detection Completed")

print(
    f"Duplicate Groups Found: "
    f"{duplicate_groups}"
)

print(
    f"Duplicate Images Found: "
    f"{duplicate_images}"
)

print(
    f"Duplicate Percentage: "
    f"{duplicate_percentage}%"
)

print(
    f"CSV Report Saved: "
    f"{csv_path}"
)

print(
    f"Summary Saved: "
    f"{json_path}"
)