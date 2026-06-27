import os
import json
import pandas as pd
from pathlib import Path
from PIL import Image

# =====================================================
# CONFIG
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PLANTVILLAGE = PROJECT_ROOT / "dataset/raw/plantvillage"
PLANTDOC = PROJECT_ROOT / "dataset/raw/plantdoc"
IP102 = PROJECT_ROOT / "dataset/raw/ip102"

REPORT_DIR = PROJECT_ROOT / "dataset/reports/statistics_report"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

# =====================================================
# HELPERS
# =====================================================

def image_resolution(image_path):
    try:
        with Image.open(image_path) as img:
            return img.size
    except:
        return None


# =====================================================
# PLANTVILLAGE
# =====================================================

def analyze_plantvillage():

    class_stats = []

    widths = []
    heights = []

    total_size = 0

    for class_dir in PLANTVILLAGE.iterdir():

        if not class_dir.is_dir():
            continue

        images = [
            f for f in class_dir.iterdir()
            if f.suffix.lower() in VALID_EXTENSIONS
        ]

        class_stats.append({
            "dataset": "PlantVillage",
            "class": class_dir.name,
            "image_count": len(images)
        })

        for img in images[:50]:

            res = image_resolution(img)

            if res:
                widths.append(res[0])
                heights.append(res[1])

        for img in images:
            total_size += img.stat().st_size

    return class_stats, widths, heights, total_size


# =====================================================
# PLANTDOC
# =====================================================

def analyze_plantdoc():

    class_counts = {}

    widths = []
    heights = []

    total_size = 0

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

            class_counts[class_dir.name] = \
                class_counts.get(class_dir.name, 0) + len(images)

            for img in images[:20]:

                res = image_resolution(img)

                if res:
                    widths.append(res[0])
                    heights.append(res[1])

            for img in images:
                total_size += img.stat().st_size

    class_stats = []

    for cls, count in class_counts.items():
        class_stats.append({
            "dataset": "PlantDoc",
            "class": cls,
            "image_count": count
        })

    return class_stats, widths, heights, total_size


# =====================================================
# IP102
# =====================================================

def analyze_ip102():

    all_labels = []

    for file_name in ["train.txt", "val.txt", "test.txt"]:

        path = IP102 / file_name

        with open(path) as f:

            for line in f:

                image_name, class_id = line.strip().split()

                all_labels.append(class_id)

    class_series = pd.Series(all_labels)

    class_counts = class_series.value_counts()

    class_stats = []

    for class_id, count in class_counts.items():

        class_stats.append({
            "dataset": "IP102",
            "class": class_id,
            "image_count": count
        })

    widths = []
    heights = []

    image_folder = IP102 / "images"

    sample_images = list(image_folder.glob("*.jpg"))[:500]

    for img in sample_images:

        res = image_resolution(img)

        if res:
            widths.append(res[0])
            heights.append(res[1])

    total_size = sum(
        f.stat().st_size
        for f in image_folder.glob("*.jpg")
    )

    return class_stats, widths, heights, total_size


# =====================================================
# MAIN
# =====================================================

all_stats = []

dataset_summary = []

for analyzer in [
    analyze_plantvillage,
    analyze_plantdoc,
    analyze_ip102
]:

    stats, widths, heights, total_size = analyzer()

    all_stats.extend(stats)

    dataset_name = stats[0]["dataset"]

    dataset_summary.append({
        "dataset": dataset_name,
        "total_classes": len(stats),
        "total_images": sum(x["image_count"] for x in stats),
        "avg_width": round(sum(widths)/len(widths), 2),
        "avg_height": round(sum(heights)/len(heights), 2),
        "dataset_size_mb": round(total_size/(1024**2), 2)
    })

# =====================================================
# SAVE REPORTS
# =====================================================

class_df = pd.DataFrame(all_stats)
summary_df = pd.DataFrame(dataset_summary)

class_df.to_csv(
    REPORT_DIR / "class_distribution.csv",
    index=False
)

summary_df.to_csv(
    REPORT_DIR / "dataset_statistics.csv",
    index=False
)

summary_df.to_json(
    REPORT_DIR / "dataset_statistics.json",
    orient="records",
    indent=4
)

summary_df.to_csv(
    REPORT_DIR / "dataset_size_report.csv",
    index=False
)

summary_df.to_csv(
    REPORT_DIR / "average_resolution_report.csv",
    index=False
)

print("\nDataset Statistics Generated Successfully")
print(summary_df)