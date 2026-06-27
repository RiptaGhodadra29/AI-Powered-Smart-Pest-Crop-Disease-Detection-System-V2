from pathlib import Path
import pandas as pd
import json

PROJECT_ROOT = Path(__file__).resolve().parents[2]

METADATA_DIR = PROJECT_ROOT / "dataset/metadata"

disease_file = (
    METADATA_DIR /
    "Disease_Class_Mapping.csv"
)

pest_file = (
    METADATA_DIR /
    "Pest_Class_Mapping.csv"
)

# =====================================
# LOAD DATA
# =====================================

disease_df = pd.read_csv(disease_file)

pest_df = pd.read_csv(pest_file)

disease_classes = sorted(
    disease_df["standardized_class"]
    .unique()
    .tolist()
)

pest_classes = sorted(
    pest_df["standardized_class"]
    .unique()
    .tolist()
)

all_classes = disease_classes + pest_classes

# =====================================
# CREATE MAPPINGS
# =====================================

class_to_id = {
    cls_name: idx
    for idx, cls_name
    in enumerate(all_classes)
}

id_to_class = {
    idx: cls_name
    for idx, cls_name
    in enumerate(all_classes)
}

# =====================================
# SAVE JSON FILES
# =====================================

with open(
    METADATA_DIR /
    "class_to_id.json",
    "w"
) as f:
    json.dump(
        class_to_id,
        f,
        indent=4
    )

with open(
    METADATA_DIR /
    "id_to_class.json",
    "w"
) as f:
    json.dump(
        id_to_class,
        f,
        indent=4
    )

# =====================================
# REPORT
# =====================================

report_df = pd.DataFrame({
    "class_name": all_classes,
    "class_id": range(len(all_classes))
})

report_path = (
    METADATA_DIR /
    "label_encoder_report.csv"
)

report_df.to_csv(
    report_path,
    index=False
)

print("\nLabel Encoding Completed")
print(
    f"Total Classes: {len(all_classes)}"
)

print(
    "Files Generated:"
)

print("class_to_id.json")
print("id_to_class.json")
print("label_encoder_report.csv")