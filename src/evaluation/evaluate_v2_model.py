from pathlib import Path
import torch
from sklearn.metrics import classification_report, confusion_matrix
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

from src.models.efficientnet_b0 import EfficientNetB0
from src.data_preparation.transforms import get_test_transforms
from src.data_preparation.dataset_loader import AlbumentationsDataset

# =========================
# Config
# =========================

NUM_CLASSES = 60
BATCH_SIZE = 16

MODEL_PATH = (
    Path("artifacts/models/best_model.pth")
)

DATASET_PATH = (
    Path("dataset/final_dataset_v2/test")
)

# =========================
# Device
# =========================

if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print(f"Using Device: {device}")

# =========================
# Dataset
# =========================

dataset = ImageFolder(DATASET_PATH)

class_names = dataset.classes

dataset = AlbumentationsDataset(
    dataset,
    transform=get_test_transforms()
)

loader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=False,
    num_workers=0,
    pin_memory=False
)

# =========================
# Model
# =========================

model = EfficientNetB0(
    num_classes=NUM_CLASSES,
    pretrained=False,
    freeze_features=False
)

model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location=device
    )
)

model.to(device)
model.eval()
print(f"Total Test Images: {len(dataset)}")

# =========================
# Evaluation
# =========================

all_labels = []
all_predictions = []

with torch.no_grad():

    for images, labels in loader:

        images = images.to(device)

        outputs = model(images)

        predictions = torch.argmax(
            outputs,
            dim=1
        )

        all_predictions.extend(
            predictions.cpu().numpy()
        )

        all_labels.extend(
            labels.numpy()
        )

# =========================
# Classification Report
# =========================

report = classification_report(
    all_labels,
    all_predictions,
    target_names=class_names,
    digits=4
)

print("\n")
print("=" * 80)
print("CLASSIFICATION REPORT")
print("=" * 80)
print(report)

# =========================
# Confusion Matrix
# =========================

cm = confusion_matrix(
    all_labels,
    all_predictions
)

print("\n")
print("=" * 80)
print("CONFUSION MATRIX SHAPE")
print("=" * 80)
print(cm.shape)

# =========================
# Unknown Crop Metrics
# =========================

unknown_index = class_names.index(
    "Unknown_Crop"
)

tp = cm[unknown_index][unknown_index]

total_unknown = cm[unknown_index].sum()

predicted_unknown = cm[:, unknown_index].sum()

recall = tp / total_unknown

precision = tp / predicted_unknown

print("\n")
print("=" * 80)
print("UNKNOWN CROP RESULTS")
print("=" * 80)

print(f"TP: {tp}")
print(f"Total Unknown Images: {total_unknown}")
print(f"Predicted Unknown: {predicted_unknown}")

print(f"Unknown Recall: {recall:.4f}")
print(f"Unknown Precision: {precision:.4f}")

