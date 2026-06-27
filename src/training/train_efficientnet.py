from pathlib import Path

import torch
import torch.nn as nn
import torch.optim as optim

from src.models.efficientnet_b0 import EfficientNetB0
from src.data_preparation.dataset_loader import create_dataloaders
from src.training.trainer import Trainer
from src.training.utils import EarlyStopping


# ======================================
# Configuration
# ======================================

NUM_CLASSES = 34

BATCH_SIZE = 16

EPOCHS = 20

LEARNING_RATE = 0.001

WEIGHT_DECAY = 0.0001


# ======================================
# Device
# ======================================

if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

print(f"\nUsing Device: {device}")


# ======================================
# Dataset
# ======================================

dataset_root = (
    Path(__file__)
    .resolve()
    .parents[2]
    / "dataset"
    / "final_dataset_v2"
)

train_loader, val_loader, _ = create_dataloaders(
    dataset_root=dataset_root,
    batch_size=BATCH_SIZE
)


# ======================================
# Model
# ======================================

model = EfficientNetB0(
    num_classes=NUM_CLASSES,
    pretrained=True,
    freeze_features=False
)

model.to(device)


# ======================================
# Loss Function
# ======================================

criterion = nn.CrossEntropyLoss()


# ======================================
# Optimizer
# ======================================

optimizer = optim.AdamW(
    model.parameters(),
    lr=LEARNING_RATE,
    weight_decay=WEIGHT_DECAY
)


# ======================================
# Scheduler
# ======================================

scheduler = optim.lr_scheduler.CosineAnnealingLR(
    optimizer,
    T_max=EPOCHS
)


# ======================================
# Early Stopping
# ======================================

early_stopping = EarlyStopping(
    patience=5
)


# ======================================
# Trainer
# ======================================

trainer = Trainer(
    model=model,
    train_loader=train_loader,
    val_loader=val_loader,
    optimizer=optimizer,
    criterion=criterion,
    scheduler=scheduler,
    device=device
)


# ======================================
# Training
# ======================================

trainer.fit(
    epochs=EPOCHS,
    early_stopping=early_stopping
)

print("\nEfficientNet-B0 Training Complete")