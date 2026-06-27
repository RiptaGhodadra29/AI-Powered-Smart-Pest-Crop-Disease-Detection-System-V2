from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
import shutil
import json

# =====================================
# CONFIG
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SOURCE_DIR = (
    PROJECT_ROOT /
    "dataset/resized/plantvillage"
)

OUTPUT_DIR = (
    PROJECT_ROOT /
    "dataset/final_dataset"
)

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

# =====================================
# BUILD IMAGE LIST
# =====================================

records = []

for class_dir in SOURCE_DIR.iterdir():

    if not class_dir.is_dir():
        continue

    class_name = class_dir.name

    for image_path in class_dir.glob("*"):

        records.append({
            "image_path": str(image_path),
            "class_name": class_name
        })

df = pd.DataFrame(records)

print(
    f"Total Images: {len(df)}"
)

# =====================================
# SPLIT
# =====================================

train_df, temp_df = train_test_split(
    df,
    test_size=0.30,
    stratify=df["class_name"],
    random_state=42
)

val_df, test_df = train_test_split(
    temp_df,
    test_size=0.50,
    stratify=temp_df["class_name"],
    random_state=42
)

print(
    f"Train: {len(train_df)}"
)

print(
    f"Validation: {len(val_df)}"
)

print(
    f"Test: {len(test_df)}"
)

# =====================================
# COPY FILES
# =====================================

def copy_split(split_df, split_name):

    for _, row in split_df.iterrows():

        src = Path(
            row["image_path"]
        )

        class_name = row["class_name"]

        dst_dir = (
            OUTPUT_DIR /
            split_name /
            class_name
        )

        dst_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(
            src,
            dst_dir / src.name
        )

copy_split(
    train_df,
    "train"
)

copy_split(
    val_df,
    "validation"
)

copy_split(
    test_df,
    "test"
)

# =====================================
# REPORT
# =====================================

summary = {
    "total_images": len(df),
    "train_images": len(train_df),
    "validation_images": len(val_df),
    "test_images": len(test_df),
    "split_ratio": "70/15/15"
}

summary_path = (
    REPORT_DIR /
    "dataset_split_report.json"
)

with open(summary_path, "w") as f:
    json.dump(
        summary,
        f,
        indent=4
    )

print(
    "\nDataset Splitting Completed"
)

print(
    f"Report Saved: {summary_path}"
)