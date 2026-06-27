from pathlib import Path
from PIL import Image
import pandas as pd
import json
from datetime import datetime

# ==========================================
# CONFIG
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_DIR = PROJECT_ROOT / "dataset/processed"

OUTPUT_DIR = PROJECT_ROOT / "dataset/resized"

REPORT_DIR = (
    PROJECT_ROOT /
    "dataset/reports/preprocessing_report"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

TARGET_SIZE = (224, 224)

VALID_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png"
)

resize_records = []

all_images = [
    f for f in INPUT_DIR.rglob("*")
    if f.suffix.lower() in VALID_EXTENSIONS
]

print(
    f"\nTotal Images Found: {len(all_images)}"
)

# ==========================================
# RESIZE
# ==========================================

for idx, image_path in enumerate(all_images, start=1):

    if idx % 5000 == 0:
        print(
            f"Processed {idx}/{len(all_images)}"
        )

    try:

        relative_path = image_path.relative_to(
            INPUT_DIR
        )

        output_path = (
            OUTPUT_DIR /
            relative_path
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with Image.open(image_path) as img:

            original_width, original_height = img.size

            img = img.resize(
                TARGET_SIZE,
                Image.LANCZOS
            )

            img.save(
                output_path,
                quality=95
            )

        resize_records.append({
            "image": str(relative_path),
            "original_width": original_width,
            "original_height": original_height,
            "new_width": 224,
            "new_height": 224,
            "status": "Success"
        })

    except Exception as e:

        resize_records.append({
            "image": str(image_path),
            "status": "Failed",
            "error": str(e)
        })

# ==========================================
# REPORTS
# ==========================================

report_df = pd.DataFrame(
    resize_records
)

csv_path = (
    REPORT_DIR /
    "resize_report.csv"
)

report_df.to_csv(
    csv_path,
    index=False
)

summary = {
    "scan_date": str(datetime.now()),
    "total_images": len(all_images),
    "target_size": "224x224",
    "successful_images":
        len(
            report_df[
                report_df["status"] == "Success"
            ]
        ),
    "failed_images":
        len(
            report_df[
                report_df["status"] == "Failed"
            ]
        )
}

json_path = (
    REPORT_DIR /
    "resize_summary.json"
)

with open(json_path, "w") as f:
    json.dump(summary, f, indent=4)

print("\nImage Resizing Completed")
print(f"CSV Report: {csv_path}")
print(f"Summary: {json_path}")