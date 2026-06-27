 # Baseline CNN Report

## Model Architecture

Input: 224 × 224 × 3

Conv2D(32)
→ ReLU
→ MaxPool

Conv2D(64)
→ ReLU
→ MaxPool

Conv2D(128)
→ ReLU
→ MaxPool

Flatten

Dense(256)
→ ReLU
→ Dropout(0.5)

Dense(15)

---

## Training Configuration

Batch Size: 16

Epochs: 20

Optimizer: AdamW

Learning Rate: 0.001

Loss Function: CrossEntropyLoss

Device: Apple MPS

---

## Training Results

Best Validation Accuracy: 94.99%

Best Validation Loss: 0.1855

---

## Test Evaluation Results

Accuracy: 94.38%

Precision: 94.50%

Recall: 94.38%

F1 Score: 94.36%

---

## Observations

- The model learned effectively within 20 epochs.
- Training and validation curves show stable convergence.
- Potato healthy class achieved excellent performance.
- Tomato Early Blight remains relatively difficult compared to other classes.
- Overall classification performance exceeded 94% accuracy.

---

## Conclusion

The Baseline CNN achieved strong performance and provides a solid benchmark for future transfer learning experiments. The model demonstrates good generalization and can be used as a reference point for comparing advanced architectures such as ResNet50, EfficientNet, and MobileNetV3.