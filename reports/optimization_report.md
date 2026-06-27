# Phase 6.9 – Pest Detection Optimization Report

## Objective

The objective of this phase was to analyze the performance of the trained YOLO11s pest detection model and identify possible improvements to increase detection accuracy, recall, and robustness.

---

## Baseline Model Information

Model: YOLO11s

Training Configuration:
- Image Size: 640 × 640
- Batch Size: 8
- Epochs: 100
- Device: Apple M1 (MPS)

Dataset:
- Total Pest Classes: 12
- Training Images: 11,500+
- Validation Images: 1,095
- Test Images: 546

---

## Baseline Performance

| Metric | Value |
|----------|----------|
| Precision | 0.844 |
| Recall | 0.745 |
| mAP@50 | 0.782 |
| mAP@50-95 | 0.473 |

---

## Class-wise Performance Analysis

### Best Performing Classes

| Class | mAP@50 |
|---------|---------|
| Weevils | 0.991 |
| Wasps | 0.987 |
| Moths | 0.968 |
| Bees | 0.906 |

These classes achieved very high detection accuracy and were easily distinguishable by the model.

---

### Moderate Performing Classes

| Class | mAP@50 |
|---------|---------|
| Ants | 0.785 |
| Earwigs | 0.793 |
| Slugs | 0.774 |
| Snails | 0.847 |
| Beetles | 0.701 |

These classes performed reasonably well but still have room for improvement.

---

### Weak Performing Classes

| Class | mAP@50 |
|---------|---------|
| Caterpillars | 0.522 |
| Earthworms | 0.529 |
| Grasshoppers | 0.576 |

These classes showed lower detection accuracy compared to other pest categories.

---

## Confusion Matrix Analysis

The normalized confusion matrix revealed that:

- Caterpillars were frequently missed.
- Earthworms showed high background confusion.
- Grasshoppers were occasionally confused with other insects.
- Small pest objects were more difficult to detect than large pests.

---

## F1 Score Analysis

The F1-Confidence Curve showed:

- Maximum F1 Score ≈ 0.78
- Optimal Confidence Threshold ≈ 0.37

This threshold provides the best balance between precision and recall.

---

## Precision-Recall Analysis

Observations:

- Moths, Wasps, and Weevils achieved excellent precision-recall performance.
- Caterpillars and Earthworms exhibited lower recall values.
- Overall model performance remained stable across most classes.

---

## Optimization Opportunities Identified

The following improvements were identified:

1. Increase image resolution.
2. Train for additional epochs.
3. Collect more samples for weak classes.
4. Apply stronger data augmentation.
5. Experiment with larger YOLO variants.
6. Improve class balance in the dataset.

---

## Final Optimization Decision

The current YOLO11s model was retained as the baseline pest detection model because:

- It achieved strong overall performance.
- Training time remained reasonable.
- Inference speed was suitable for deployment.
- Accuracy was sufficient for the project requirements.

---

## Conclusion

The YOLO11s pest detection model successfully learned all 12 pest categories and achieved strong overall detection performance.

Final Results:

- Precision: 0.844
- Recall: 0.745
- mAP@50: 0.782
- mAP@50-95: 0.473

The model is suitable for integration into the Smart Pest & Crop Disease Detection System.