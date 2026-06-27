from pathlib import Path
import pandas as pd
import json
from datetime import datetime

# ==================================================
# CONFIG
# ==================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PLANTVILLAGE = PROJECT_ROOT / "dataset/raw/plantvillage"
PLANTDOC = PROJECT_ROOT / "dataset/raw/plantdoc"
IP102 = PROJECT_ROOT / "dataset/raw/ip102"

REPORT_DIR = (
    PROJECT_ROOT /
    "dataset/reports/validation_report"
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

issues = []

# ==================================================
# PLANTVILLAGE VALIDATION
# ==================================================

print("\nChecking PlantVillage...")

for class_dir in PLANTVILLAGE.iterdir():

    if not class_dir.is_dir():
        continue

    images = [
        f for f in class_dir.iterdir()
        if f.suffix.lower() in VALID_EXTENSIONS
    ]

    if len(images) == 0:

        issues.append({
            "dataset": "PlantVillage",
            "issue": "Empty Class",
            "path": str(class_dir)
        })

# ==================================================
# PLANTDOC VALIDATION
# ==================================================

print("Checking PlantDoc...")

for split in ["train", "test"]:

    split_path = PLANTDOC / split

    if not split_path.exists():
        continue

    for class_dir in split_path.iterdir():

        if not class_dir.is_dir():
            continue

        images = [
            f for f in class_dir.iterdir()
            if f.suffix.lower() in VALID_EXTENSIONS
        ]

        if len(images) == 0:

            issues.append({
                "dataset": "PlantDoc",
                "issue": "Empty Class",
                "path": str(class_dir)
            })

# ==================================================
# IP102 VALIDATION
# ==================================================

print("Checking IP102...")

image_folder = IP102 / "images"

all_classes = set()

for annotation_file in [
    "train.txt",
    "val.txt",
    "test.txt"
]:

    file_path = IP102 / annotation_file

    if not file_path.exists():

        issues.append({
            "dataset": "IP102",
            "issue": "Missing Annotation File",
            "path": str(file_path)
        })

        continue

    with open(file_path, "r") as f:

        lines = f.readlines()

    for line_no, line in enumerate(lines, start=1):

        line = line.strip()

        if not line:

            issues.append({
                "dataset": "IP102",
                "issue": "Empty Annotation Line",
                "file": annotation_file,
                "line": line_no
            })

            continue

        parts = line.split()

        if len(parts) != 2:

            issues.append({
                "dataset": "IP102",
                "issue": "Invalid Annotation Format",
                "file": annotation_file,
                "line": line_no
            })

            continue

        image_name, label = parts

        image_path = image_folder / image_name

        if not image_path.exists():

            issues.append({
                "dataset": "IP102",
                "issue": "Missing Image",
                "path": str(image_path)
            })

        all_classes.add(label)

# ==================================================
# CHECK CLASS COUNT
# ==================================================

if len(all_classes) == 0:

    issues.append({
        "dataset": "IP102",
        "issue": "No Classes Found"
    })

# ==================================================
# SAVE REPORT
# ==================================================

report_df = pd.DataFrame(issues)

csv_path = (
    REPORT_DIR /
    "missing_data_report.csv"
)

report_df.to_csv(
    csv_path,
    index=False
)

summary = {
    "scan_date": str(datetime.now()),
    "issues_found": len(issues),
    "datasets_checked": 3,
    "status":
        "PASSED"
        if len(issues) == 0
        else "FAILED"
}

json_path = (
    REPORT_DIR /
    "missing_data_summary.json"
)

with open(json_path, "w") as f:
    json.dump(summary, f, indent=4)

print("\nMissing Data Validation Completed")
print(f"Issues Found: {len(issues)}")
print(f"CSV Report: {csv_path}")
print(f"Summary Report: {json_path}")