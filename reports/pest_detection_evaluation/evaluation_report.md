# Phase 6.8 – Pest Detection Evaluation & Result Analysis

## Project Title

AI-Powered Smart Pest & Crop Disease Detection System

---

# 1. Objective

The objective of this phase was to evaluate the performance of the trained YOLO11s pest detection model on unseen test data and analyze its effectiveness in detecting different pest classes.

---

# 2. Model Information

| Parameter | Value |
|------------|---------|
| Model | YOLO11s |
| Training Method | Transfer Learning |
| Input Image Size | 640 × 640 |
| Epochs | 100 (Training Run) |
| Batch Size | 8 |
| Device | Apple M1 (MPS) |
| Number of Classes | 12 |

---

# 3. Test Dataset Information

| Item | Value |
|--------|--------|
| Test Images | 546 |
| Total Pest Instances | 689 |
| Number of Classes | 12 |

---

# 4. Overall Model Performance

| Metric | Score |
|----------|---------|
| Precision | 0.844 |
| Recall | 0.745 |
| mAP@50 | 0.782 |
| mAP@50-95 | 0.473 |

---

# 5. Metric Interpretation

## Precision (84.4%)

Precision measures how many detected pests are actually correct.

A precision score of 84.4% indicates that most of the model's detections are accurate and only a small number of false detections occur.

---

## Recall (74.5%)

Recall measures how many actual pests present in the images are successfully detected by the model.

A recall score of 74.5% indicates that the model can identify the majority of pest instances, although some pests are still missed.

---

## mAP@50 (78.2%)

mAP@50 evaluates detection performance using a 50% Intersection over Union (IoU) threshold.

The obtained score of 78.2% demonstrates strong object detection capability and good localization performance.

---

## mAP@50-95 (47.3%)

This metric evaluates performance across multiple IoU thresholds from 50% to 95%.

The score of 47.3% indicates that while the model detects pests successfully, there is still room for improvement in bounding box precision.

---

# 6. Class-Wise Performance Analysis

| Pest Class | Precision | Recall | mAP@50 | mAP@50-95 |
|------------|-----------|---------|---------|------------|
| Ants | 0.886 | 0.716 | 0.785 | 0.350 |
| Bees | 0.860 | 0.909 | 0.906 | 0.466 |
| Beetles | 0.742 | 0.636 | 0.701 | 0.409 |
| Caterpillars | 0.785 | 0.433 | 0.522 | 0.256 |
| Earthworms | 0.641 | 0.500 | 0.529 | 0.255 |
| Earwigs | 0.939 | 0.628 | 0.793 | 0.389 |
| Grasshoppers | 0.769 | 0.618 | 0.576 | 0.305 |
| Moths | 0.990 | 0.936 | 0.968 | 0.793 |
| Slugs | 0.781 | 0.767 | 0.774 | 0.479 |
| Snails | 0.854 | 0.840 | 0.847 | 0.614 |
| Wasps | 0.965 | 0.979 | 0.987 | 0.650 |
| Weevils | 0.919 | 0.982 | 0.991 | 0.706 |

---

# 7. Best Performing Classes

The highest-performing pest classes were:

1. Weevils
   - mAP@50 = 99.1%

2. Wasps
   - mAP@50 = 98.7%

3. Moths
   - mAP@50 = 96.8%

These classes were detected with very high accuracy and strong localization performance.

---

# 8. Weak Performing Classes

The lowest-performing pest classes were:

1. Caterpillars
   - mAP@50 = 52.2%

2. Earthworms
   - mAP@50 = 52.9%

3. Grasshoppers
   - mAP@50 = 57.6%

These classes require further improvement through additional data collection, annotation refinement, and training optimization.

---

# 9. Possible Reasons for Lower Performance

Several factors may have contributed to lower detection accuracy for certain classes:

- Limited number of training images.
- Similar visual appearance between pest species.
- Small object sizes in images.
- Complex backgrounds.
- Occlusions and overlapping objects.
- Imperfect bounding box annotations.

---

# 10. Model Strengths

The trained YOLO11s model demonstrated several strengths:

- Successfully detects 12 pest classes.
- High precision (84.4%).
- Good recall performance (74.5%).
- Strong mAP@50 score (78.2%).
- Effective transfer learning capability.
- Real-time detection potential.
- Good generalization on unseen test data.

---

# 11. Model Limitations

The following limitations were observed:

- Lower performance for Caterpillars, Earthworms, and Grasshoppers.
- Some missed pest detections.
- Bounding box localization can be improved.
- Performance may vary under challenging field conditions.

---

# 12. Recommendations for Improvement

Future optimization strategies include:

- Collect more images for weak classes.
- Improve annotation quality.
- Increase training epochs.
- Experiment with larger YOLO models.
- Apply advanced data augmentation techniques.
- Perform hyperparameter tuning.
- Use higher-resolution input images.

---

# 13. Final Conclusion

The YOLO11s pest detection model achieved strong overall performance on the AgriPest dataset. The model obtained a Precision of 84.4%, Recall of 74.5%, mAP@50 of 78.2%, and mAP@50-95 of 47.3%. The results demonstrate that transfer learning with YOLO11s is effective for multi-class agricultural pest detection.

The model showed excellent performance for Weevils, Wasps, and Moths while comparatively lower performance was observed for Caterpillars, Earthworms, and Grasshoppers. Overall, the trained model is suitable for real-time pest detection applications and provides a strong foundation for further optimization and deployment.

---

# Phase Status

## Completed Work

- Pest Dataset Collection
- Pest Annotation Verification
- YOLO Dataset Preparation
- YOLO Environment Setup
- YOLO Model Training
- Pest Detection Testing
- Pest Detection Evaluation

