import random
from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image

# ==========================================
# CONFIG
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PLANTVILLAGE = PROJECT_ROOT / "dataset/raw/plantvillage"
PLANTDOC = PROJECT_ROOT / "dataset/raw/plantdoc"
IP102 = PROJECT_ROOT / "dataset/raw/ip102"

EDA_DIR = PROJECT_ROOT / "dataset/reports/eda_report"

RANDOM_DIR = EDA_DIR / "random_samples"
CLASS_DIR = EDA_DIR / "class_samples"
DISEASE_DIR = EDA_DIR / "disease_examples"
PEST_DIR = EDA_DIR / "pest_examples"

for folder in [
    RANDOM_DIR,
    CLASS_DIR,
    DISEASE_DIR,
    PEST_DIR
]:
    folder.mkdir(parents=True, exist_ok=True)

VALID_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
)

# ==========================================
# HELPERS
# ==========================================

def get_images(folder):
    return [
        f for f in folder.rglob("*")
        if f.suffix.lower() in VALID_EXTENSIONS
    ]


def save_grid(images, title, output_path, cols=4):

    rows = (len(images) + cols - 1) // cols

    plt.figure(figsize=(15, rows * 4))

    for i, image_path in enumerate(images):

        plt.subplot(rows, cols, i + 1)

        img = Image.open(image_path)

        plt.imshow(img)

        plt.title(image_path.parent.name[:25])

        plt.axis("off")

    plt.suptitle(title)

    plt.tight_layout()

    plt.savefig(output_path, dpi=300)

    plt.close()


# ==========================================
# RANDOM SAMPLES
# ==========================================

all_images = []

all_images.extend(get_images(PLANTVILLAGE))
all_images.extend(get_images(PLANTDOC))
all_images.extend(get_images(IP102 / "images"))

random_samples = random.sample(
    all_images,
    min(20, len(all_images))
)

save_grid(
    random_samples,
    "Random Dataset Samples",
    RANDOM_DIR / "random_samples.png"
)

# ==========================================
# CLASS SAMPLES
# ==========================================

class_images = []

for class_dir in PLANTVILLAGE.iterdir():

    if not class_dir.is_dir():
        continue

    imgs = get_images(class_dir)

    if imgs:
        class_images.append(imgs[0])

save_grid(
    class_images[:20],
    "PlantVillage Class Samples",
    CLASS_DIR / "plantvillage_classes.png"
)

# ==========================================
# DISEASE EXAMPLES
# ==========================================

disease_images = []

for split in ["train", "test"]:

    split_path = PLANTDOC / split

    if not split_path.exists():
        continue

    for class_dir in split_path.iterdir():

        if not class_dir.is_dir():
            continue

        imgs = get_images(class_dir)

        if imgs:
            disease_images.append(imgs[0])

save_grid(
    disease_images[:20],
    "PlantDoc Disease Examples",
    DISEASE_DIR / "plantdoc_diseases.png"
)

# ==========================================
# PEST EXAMPLES
# ==========================================

pest_images = get_images(IP102 / "images")

pest_examples = random.sample(
    pest_images,
    min(20, len(pest_images))
)

save_grid(
    pest_examples,
    "IP102 Pest Examples",
    PEST_DIR / "ip102_pests.png"
)

print("\nEDA Visualizations Generated Successfully")