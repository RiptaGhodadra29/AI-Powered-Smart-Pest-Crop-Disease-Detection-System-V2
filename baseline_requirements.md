# 🧠 Baseline Model Development Requirements  
## AI-Powered Smart Pest & Crop Disease Detection System

---

## A. Objective

The objective of this phase is to define a clear understanding of the **baseline model** before starting model development.

We aim to establish:
- What a baseline model is
- Why it is required in this project
- What inputs and outputs it will handle
- Its limitations and constraints
- How we will measure its success

This ensures a structured and measurable starting point for AI model development.

---

## B. Why This Phase Is Needed

A baseline model is important because:

- It provides the first working version of the AI system
- It helps validate dataset quality and preprocessing pipeline
- It acts as a performance benchmark for future improvements
- It helps identify errors early in data or labels
- It ensures end-to-end system functionality before optimization

Without a baseline model, it is impossible to measure improvement effectively.

---

## C. Theory (Simple Explanation)

A baseline model is the simplest working AI model for a problem.

In this project:

Input → Crop Image  
Output → Disease or Pest Class Prediction

A baseline model:
- Uses simple architecture (basic CNN or pretrained model)
- Focuses on working pipeline, not high accuracy
- Ensures system correctness end-to-end

Think of it as:
👉 “First working prototype of the AI system”

---

## D. Available Options for Baseline Model

### 1. Simple CNN (From Scratch)
- Built using convolution layers
- Learns features directly from dataset
- No pretrained knowledge used

### 2. Transfer Learning Model
- Uses pretrained models trained on ImageNet
- Examples: ResNet, MobileNet, EfficientNet
- Only final layers are trained on our dataset

### 3. Hybrid Approach
- Combination of CNN + feature engineering
- Rarely used in modern deep learning pipelines

---

## E. Advantages of Baseline Model

- Validates full AI pipeline
- Detects dataset and label issues early
- Provides performance reference for comparison
- Helps debug preprocessing and training steps
- Fast to implement compared to advanced models

---

## F. Disadvantages of Baseline Model

- Lower accuracy compared to optimized models
- Limited ability to handle complex patterns
- May misclassify visually similar diseases
- Not suitable for production deployment
- Limited generalization capability

---

## G. Industry Best Practices

Industry professionals follow these practices:

- Always start with a baseline model
- Keep architecture simple initially
- Validate dataset before model complexity
- Track baseline performance metrics
- Use baseline as comparison reference for improvements

---

## H. Recommendation Criteria

A good baseline model should:

- Train quickly and efficiently
- Work on cleaned and preprocessed dataset
- Support multi-class classification
- Be easy to debug and interpret
- Provide measurable performance metrics
- Allow future upgrade to advanced models

---

## I. Deliverables of This Phase

- Clear definition of baseline model
- Input/output specification
- Constraints and risks
- Success criteria
- Evaluation approach
- Baseline readiness checklist

---

## J. Common Mistakes to Avoid

- Starting with complex models too early
- Ignoring dataset quality issues
- Skipping baseline evaluation
- Not defining success metrics
- Overfocusing on accuracy instead of pipeline stability

---

## K. Pre-Requisites Before Next Phase

Before moving to the next phase:

- Dataset is cleaned and validated
- Train/validation/test split is ready
- Labels are encoded properly
- Preprocessing pipeline is stable
- Problem is clearly defined as image classification

---

## 📌 Summary

The baseline model is the first working version of the AI system that helps validate the dataset, pipeline, and overall architecture before moving to advanced models.

This ensures a strong foundation for future improvements.