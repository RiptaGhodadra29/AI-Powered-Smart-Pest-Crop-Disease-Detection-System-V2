import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CONFIG_PATH = (
    PROJECT_ROOT /
    "src/data_preparation/augmentation_config.json"
)

with open(CONFIG_PATH) as f:
    config = json.load(f)

augmentation_report = {
    "augmentation_type": "Online Training-Time Augmentation",
    "rotation_degrees": config["rotation"],
    "horizontal_flip": config["horizontal_flip"],
    "zoom_range": [
        config["zoom_scale_min"],
        config["zoom_scale_max"]
    ],
    "brightness": config["brightness"],
    "contrast": config["contrast"],
    "status": "Approved"
}

REPORT_PATH = (
    PROJECT_ROOT /
    "dataset/reports/preprocessing_report/augmentation_report.json"
)

with open(REPORT_PATH, "w") as f:
    json.dump(
        augmentation_report,
        f,
        indent=4
    )

print("\nAugmentation Configuration Created")
print(f"Saved: {REPORT_PATH}")