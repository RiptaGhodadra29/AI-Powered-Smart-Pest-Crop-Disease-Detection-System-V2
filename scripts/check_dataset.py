from PIL import Image
from pathlib import Path

dataset = Path("dataset/final_dataset_v2/train")

bad = []

for img_path in dataset.rglob("*"):
    if img_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]:
        try:
            img = Image.open(img_path)
            img.verify()
        except Exception:
            bad.append(str(img_path))

print(f"Bad Images: {len(bad)}")

for b in bad:
    print(b)