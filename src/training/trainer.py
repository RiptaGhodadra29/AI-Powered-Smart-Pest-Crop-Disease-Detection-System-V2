import os
import torch
import torch.nn as nn
from tqdm import tqdm
from torch.utils.tensorboard import SummaryWriter


class Trainer:
    def __init__(
        self,
        model,
        train_loader,
        val_loader,
        optimizer,
        criterion,
        scheduler,
        device
    ):
        self.model = model
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.optimizer = optimizer
        self.criterion = criterion
        self.scheduler = scheduler
        self.device = device

        # TensorBoard
        self.writer = SummaryWriter("runs/crop_disease_experiment")

    # -------------------------
    # TRAIN ONE EPOCH
    # -------------------------
    def train_one_epoch(self):
        self.model.train()
        total_loss = 0

        for images, labels in tqdm(self.train_loader):
            images = images.to(self.device)
            labels = labels.to(self.device)

            outputs = self.model(images)
            loss = self.criterion(outputs, labels)

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            total_loss += loss.item()

        return total_loss / len(self.train_loader)

    # -------------------------
    # VALIDATION
    # -------------------------
    def validate(self):
        self.model.eval()
        total_loss = 0
        correct = 0
        total = 0

        with torch.no_grad():
            for images, labels in self.val_loader:
                images = images.to(self.device)
                labels = labels.to(self.device)

                outputs = self.model(images)
                loss = self.criterion(outputs, labels)

                total_loss += loss.item()

                _, predicted = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        accuracy = 100 * correct / total
        return total_loss / len(self.val_loader), accuracy

    # -------------------------
    # FULL TRAINING LOOP
    # -------------------------
    def fit(self, epochs, early_stopping=None):

        # ✅ FIX: Ensure folders exist BEFORE training starts
        os.makedirs("artifacts/models", exist_ok=True)
        os.makedirs("artifacts/logs", exist_ok=True)

        best_acc = 0

        for epoch in range(epochs):

            train_loss = self.train_one_epoch()
            val_loss, val_acc = self.validate()

            # Scheduler step
            if self.scheduler:
                self.scheduler.step()

            # TensorBoard logging
            self.writer.add_scalar("Loss/Train", train_loss, epoch)
            self.writer.add_scalar("Loss/Val", val_loss, epoch)
            self.writer.add_scalar("Accuracy/Val", val_acc, epoch)

            print(f"\nEpoch [{epoch+1}/{epochs}]")
            print(f"Train Loss: {train_loss:.4f}")
            print(f"Val Loss: {val_loss:.4f}")
            print(f"Val Accuracy: {val_acc:.2f}%")

            # Save best model
            if val_acc > best_acc:
                best_acc = val_acc

                torch.save(
                    self.model.state_dict(),
                    "artifacts/models/best_model.pth"
                )

            # Early stopping
            if early_stopping:
                early_stopping(val_loss)
                if early_stopping.early_stop:
                    print("Early stopping triggered!")
                    break