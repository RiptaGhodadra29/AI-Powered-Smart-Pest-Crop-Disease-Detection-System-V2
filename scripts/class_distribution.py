from pathlib import Path
from collections import Counter

labels_dir = Path("dataset/raw/agripest")

counter = Counter()

for txt_file in labels_dir.rglob("*.txt"):
    if txt_file.stat().st_size == 0:
        continue

    with open(txt_file, "r") as f:
        for line in f:
            parts = line.strip().split()

            if len(parts) >= 5:
                class_id = int(parts[0])
                counter[class_id] += 1

class_names = [
    "Ants",
    "Bees",
    "Beetles",
    "Caterpillars",
    "Earthworms",
    "Earwigs",
    "Grasshoppers",
    "Moths",
    "Slugs",
    "Snails",
    "Wasps",
    "Weevils",
]

print("\nClass Distribution\n")
print("-" * 40)

total = sum(counter.values())

for cid, name in enumerate(class_names):
    count = counter[cid]
    pct = (count / total) * 100 if total > 0 else 0

    print(
        f"{cid:2d} | {name:<15} | {count:6d} | {pct:6.2f}%"
    )

print("-" * 40)
print(f"Total Objects: {total}")