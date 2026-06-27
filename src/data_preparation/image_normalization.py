from pathlib import Path
from PIL import Image
import numpy as np
import json

# ==========================================
# CONFIG
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET_DIR = (
    PROJECT_ROOT /
    "dataset/resized"
)

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
    ".png"
)

# ==========================================
# LOAD IMAGES
# ==========================================

all_images = [
    f for f in DATASET_DIR.rglob("*")
    if f.suffix.lower() in VALID_EXTENSIONS
]

print(
    f"\nTotal Images Found: {len(all_images)}"
)

# ==========================================
# CALCULATE MEAN / STD
# ==========================================

pixel_sum = np.zeros(3)
pixel_squared_sum = np.zeros(3)

total_pixels = 0

for idx, image_path in enumerate(all_images, start=1):

    if idx % 5000 == 0:
        print(
            f"Processed {idx}/{len(all_images)}"
        )

    image = Image.open(image_path)

    image = np.array(image) / 255.0

    pixels = image.reshape(-1, 3)

    pixel_sum += pixels.sum(axis=0)

    pixel_squared_sum += (
        pixels ** 2
    ).sum(axis=0)

    total_pixels += pixels.shape[0]

mean = pixel_sum / total_pixels

std = np.sqrt(
    pixel_squared_sum / total_pixels
    - mean**2
)

# ==========================================
# SAVE REPORT
# ==========================================

stats = {
    "mean": mean.tolist(),
    "std": std.tolist(),
    "total_images": len(all_images)
}

output_file = (
    REPORT_DIR /
    "normalization_statistics.json"
)

with open(output_file, "w") as f:
    json.dump(stats, f, indent=4)

print("\nNormalization Statistics Generated")
print(f"Mean: {mean}")
print(f"Std : {std}")
print(f"Saved: {output_file}")