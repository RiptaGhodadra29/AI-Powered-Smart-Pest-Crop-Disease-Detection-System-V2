import torch
import torch.nn as nn
from torchvision import models


class EfficientNetB0(nn.Module):
    """
    EfficientNet-B0 Transfer Learning Model for Crop Disease Classification
    """

    def __init__(self, num_classes=15, pretrained=True, freeze_features=True):
        super().__init__()

        # ==============================
        # 1. Load Pretrained EfficientNet
        # ==============================
        if pretrained:
            weights = models.EfficientNet_B0_Weights.IMAGENET1K_V1
            self.model = models.efficientnet_b0(weights=weights)
        else:
            self.model = models.efficientnet_b0(weights=None)

        # ==============================
        # 2. Freeze Feature Extractor
        # ==============================
        if freeze_features:
            for param in self.model.features.parameters():
                param.requires_grad = False

        # ==============================
        # 3. Replace Classifier
        # ==============================
        in_features = self.model.classifier[1].in_features

        self.model.classifier = nn.Sequential(
            nn.Dropout(p=0.3),
            nn.Linear(in_features, num_classes)
        )

    # ==============================
    # 4. Forward Pass
    # ==============================
    def forward(self, x):
        return self.model(x)

    # ==============================
    # 5. Utility: Unfreeze Top Layers
    # ==============================
    def unfreeze_features(self):
        """
        Unfreeze feature extractor for fine-tuning
        """
        for param in self.model.features.parameters():
            param.requires_grad = True

    # ==============================
    # 6. Utility: Freeze Again
    # ==============================
    def freeze_features(self):
        """
        Freeze feature extractor
        """
        for param in self.model.features.parameters():
            param.requires_grad = False