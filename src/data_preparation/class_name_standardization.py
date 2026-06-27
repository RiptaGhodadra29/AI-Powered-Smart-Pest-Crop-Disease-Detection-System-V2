from pathlib import Path
import pandas as pd
import re

# ==========================================
# CONFIG
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PLANTVILLAGE = PROJECT_ROOT / "dataset/raw/plantvillage"
PLANTDOC = PROJECT_ROOT / "dataset/raw/plantdoc"
IP102 = PROJECT_ROOT / "dataset/raw/ip102"

METADATA_DIR = PROJECT_ROOT / "dataset/metadata"
METADATA_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# STANDARDIZATION FUNCTION
# ==========================================

def standardize_name(name):

    name = name.strip()

    name = re.sub(r"[_]+", " ", name)

    name = re.sub(r"\s+", " ", name)

    name = name.title()

    name = name.replace(" ", "_")

    return name

# ==========================================
# DISEASE CLASSES
# ==========================================

disease_records = []

# PlantVillage

for class_dir in PLANTVILLAGE.iterdir():

    if class_dir.is_dir():

        disease_records.append({
            "dataset": "PlantVillage",
            "original_class": class_dir.name,
            "standardized_class":
                standardize_name(class_dir.name)
        })

# PlantDoc

for split in ["train", "test"]:

    split_path = PLANTDOC / split

    if not split_path.exists():
        continue

    for class_dir in split_path.iterdir():

        if class_dir.is_dir():

            disease_records.append({
                "dataset": "PlantDoc",
                "original_class": class_dir.name,
                "standardized_class":
                    standardize_name(class_dir.name)
            })

# Remove duplicates

disease_df = pd.DataFrame(
    disease_records
).drop_duplicates()

# ==========================================
# PEST CLASSES
# ==========================================

pest_records = []

for label_id in range(102):

    pest_records.append({
        "dataset": "IP102",
        "original_class": str(label_id),
        "standardized_class":
            f"Pest_Class_{label_id}"
    })

pest_df = pd.DataFrame(pest_records)

# ==========================================
# SAVE FILES
# ==========================================

disease_path = (
    METADATA_DIR /
    "Disease_Class_Mapping.csv"
)

pest_path = (
    METADATA_DIR /
    "Pest_Class_Mapping.csv"
)

report_path = (
    METADATA_DIR /
    "Updated_Class_Mapping_Report.csv"
)

disease_df.to_csv(
    disease_path,
    index=False
)

pest_df.to_csv(
    pest_path,
    index=False
)

combined_df = pd.concat([
    disease_df,
    pest_df
])

combined_df.to_csv(
    report_path,
    index=False
)

print("\nClass Standardization Completed")

print(
    f"Disease Classes: "
    f"{len(disease_df)}"
)

print(
    f"Pest Classes: "
    f"{len(pest_df)}"
)

print(
    f"Total Classes: "
    f"{len(combined_df)}"
)