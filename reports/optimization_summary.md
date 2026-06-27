# Pest Detection Optimization Summary

## Model

YOLO11s

---

## Dataset

- 12 Pest Classes
- 11,500+ Training Images
- 1,095 Validation Images
- 546 Test Images

---

## Final Performance

| Metric | Score |
|----------|----------|
| Precision | 0.844 |
| Recall | 0.745 |
| mAP@50 | 0.782 |
| mAP@50-95 | 0.473 |

---

## Strongest Classes

- Weevils
- Wasps
- Moths
- Bees

These classes achieved excellent detection performance.

---

## Weakest Classes

- Caterpillars
- Earthworms
- Grasshoppers

These classes require additional optimization and data collection.

---

## Key Findings

- The model demonstrates strong generalization ability.
- Most pest categories achieved high detection accuracy.
- Small and visually similar pests remain challenging.
- Background confusion affects some classes.

---

## Optimization Recommendations

1. Increase image size from 640 to 800.
2. Train additional epochs.
3. Improve class balancing.
4. Collect more images for weak classes.
5. Experiment with YOLO11m.

---

## Selected Final Model

YOLO11s

Reason:

Provides a good balance between:
- Accuracy
- Training Time
- Inference Speed
- Resource Consumption