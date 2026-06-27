from pathlib import Path
from PIL import Image
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = PROJECT_ROOT / "dataset/raw"

PROCESSED_DIR = (
    PROJECT_ROOT /
    "dataset/processed"
)

REPORT_DIR = (
    PROJECT_ROOT /
    "dataset/reports/preprocessing_report"
)

PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True
)

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

VALID_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png"
)

cleaning_report = []

all_images = [
    f for f in RAW_DIR.rglob("*")
    if f.suffix.lower() in VALID_EXTENSIONS
]

print(
    f"\nCleaning {len(all_images)} images..."
)

for idx, image_path in enumerate(all_images, start=1):

    if idx % 5000 == 0:
        print(
            f"Processed {idx}/{len(all_images)}"
        )

    try:

        relative_path = (
            image_path.relative_to(RAW_DIR)
        )

        output_path = (
            PROCESSED_DIR /
            relative_path
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with Image.open(image_path) as img:

            original_mode = img.mode

            img = img.convert("RGB")

            img.save(
                output_path,
                quality=95
            )

        cleaning_report.append({
            "image": str(relative_path),
            "status": "Cleaned",
            "original_mode": original_mode,
            "new_mode": "RGB"
        })

    except Exception as e:

        cleaning_report.append({
            "image": str(image_path),
            "status": "Failed",
            "error": str(e)
        })

report_df = pd.DataFrame(
    cleaning_report
)

report_path = (
    REPORT_DIR /
    "image_cleaning_report.csv"
)

report_df.to_csv(
    report_path,
    index=False
)

print("\nImage Cleaning Completed")
print(
    f"Report Saved: {report_path}"
)