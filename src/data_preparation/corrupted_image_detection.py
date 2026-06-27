from pathlib import Path
from PIL import Image
import pandas as pd
import json
from datetime import datetime

# ==================================================
# CONFIGURATION
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
# FIND ALL IMAGES
# ==================================================

all_images = [
    file
    for file in DATASET_ROOT.rglob("*")
    if file.suffix.lower() in VALID_EXTENSIONS
]

print(f"\nTotal Images Found: {len(all_images)}")

# ==================================================
# CORRUPTION CHECK
# ==================================================

corrupted_images = []

for idx, image_path in enumerate(all_images, start=1):

    if idx % 5000 == 0:
        print(f"Processed {idx}/{len(all_images)} images")

    try:

        # Verify image integrity
        with Image.open(image_path) as img:
            img.verify()

        # Re-open to validate dimensions
        with Image.open(image_path) as img:

            width, height = img.size

            if width <= 0 or height <= 0:

                corrupted_images.append({
                    "image_path": str(image_path),
                    "error_type": "Invalid Dimension",
                    "width": width,
                    "height": height
                })

    except Exception as e:

        corrupted_images.append({
            "image_path": str(image_path),
            "error_type": type(e).__name__,
            "error_message": str(e)
        })

# ==================================================
# SAVE CSV REPORT
# ==================================================

report_df = pd.DataFrame(corrupted_images)

csv_path = (
    REPORT_DIR /
    "corrupted_image_report.csv"
)

report_df.to_csv(
    csv_path,
    index=False
)

# ==================================================
# SAVE SUMMARY
# ==================================================

summary = {
    "scan_date": str(datetime.now()),
    "total_images_scanned": len(all_images),
    "corrupted_images_found": len(corrupted_images),
    "dataset_status":
        "PASSED"
        if len(corrupted_images) == 0
        else "FAILED"
}

json_path = (
    REPORT_DIR /
    "corrupted_image_summary.json"
)

with open(json_path, "w") as f:
    json.dump(summary, f, indent=4)

# ==================================================
# FINAL OUTPUT
# ==================================================

print("\nCorrupted Image Detection Completed")

print(
    f"Corrupted Images Found: "
    f"{len(corrupted_images)}"
)

print(
    f"CSV Report: {csv_path}"
)

print(
    f"Summary Report: {json_path}"
)