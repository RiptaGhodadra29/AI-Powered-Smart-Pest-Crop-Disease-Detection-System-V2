# Data Pipeline Design
## AI-Powered Smart Pest & Crop Disease Detection System

---

# A. Objective

The objective of this phase is to design a complete image preprocessing and data pipeline that prepares crop images for CNN training.

The pipeline must:

- Load images correctly
- Apply preprocessing
- Apply augmentation
- Convert images into tensors
- Create batches for training
- Feed data into the CNN model

---

# B. Why This Phase Is Needed

Raw images cannot be directly used by CNN models.

Images must be:

- Standardized
- Normalized
- Converted into tensors
- Organized into batches

A well-designed pipeline ensures:

- Consistent input quality
- Better model performance
- Faster training
- Reduced overfitting

---

# C. Technology Stack Used

Deep Learning Framework:

- PyTorch

Computer Vision Libraries:

- TorchVision
- Pillow (PIL)
- Albumentations

---

# D. Data Pipeline Overview

Image File
     ↓
Load Image
     ↓
Resize
     ↓
Augmentation (Training Only)
     ↓
Normalization
     ↓
Tensor Conversion
     ↓
Batch Creation
     ↓
CNN Model

---

# E. Dataset Structure

dataset/
└── final_dataset/
    ├── train/
    ├── validation/
    └── test/

Each folder contains class directories.

Example:

train/
├── Tomato_healthy/
├── Tomato_Early_blight/
├── Potato___Late_blight/
└── ...

---

# F. Image Input Specifications

Input Type:

- RGB Image

Supported Formats:

- JPG
- JPEG
- PNG

Target Image Size:

224 × 224

Channels:

3 (RGB)

---

# G. Training Pipeline

Training images undergo:

1. Image Loading
2. Resize
3. Data Augmentation
4. Normalization
5. Tensor Conversion
6. Batch Creation

Workflow:

Image
 ↓
Resize
 ↓
Random Augmentation
 ↓
Normalize
 ↓
Tensor
 ↓
Batch

---

# H. Training Augmentation Strategy

Purpose:

Increase dataset diversity and reduce overfitting.

Selected Augmentations:

1. Horizontal Flip

Reason:

Leaves may appear in different orientations.

---

2. Rotation

Reason:

Disease symptoms remain visible even when rotated.

---

3. Brightness Adjustment

Reason:

Images may be captured under different lighting conditions.

---

4. Contrast Adjustment

Reason:

Improves model robustness.

---

5. Random Crop

Reason:

Helps model focus on different image regions.

---

# I. Validation Pipeline

Validation data should remain unchanged.

Pipeline:

Image
 ↓
Resize
 ↓
Normalize
 ↓
Tensor

No augmentation applied.

Reason:

Validation must represent real-world data.

---

# J. Test Pipeline

Pipeline:

Image
 ↓
Resize
 ↓
Normalize
 ↓
Tensor

No augmentation applied.

Reason:

Final evaluation must use untouched data.

---

# K. Normalization Strategy

Purpose:

Bring pixel values into a consistent range.

Benefits:

- Faster convergence
- Stable training
- Better gradient flow

Workflow:

Pixel Values
(0–255)
      ↓
Scaled
      ↓
Normalized
      ↓
Tensor

---

# L. Tensor Conversion

CNN models process tensors rather than images.

Conversion:

Image
 ↓
Numeric Matrix
 ↓
Tensor

Benefits:

- GPU compatibility
- Efficient computation
- Batch processing

---

# M. Batch Processing Strategy

Selected Batch Size:

32

Reason:

- Good balance between speed and memory usage
- Suitable for baseline CNN

Workflow:

32 Images
      ↓
One Batch
      ↓
Model Training

---

# N. Data Shuffling Strategy

Training:

✓ Enabled

Reason:

Prevent learning image order.

Validation:

✗ Disabled

Test:

✗ Disabled

Reason:

Ensure consistent evaluation.

---

# O. Data Loader Responsibilities

Train Loader:

- Load images
- Apply augmentation
- Shuffle data
- Create batches

Validation Loader:

- Load images
- No augmentation
- Create batches

Test Loader:

- Load images
- No augmentation
- Create batches

---

# P. Data Integrity Verification

Before training:

Verify:

✓ Folder structure

✓ Number of classes

✓ Image count

✓ Missing images

✓ Corrupted images

✓ Label consistency

✓ Split consistency

---

# Q. Expected Outputs

The pipeline should produce:

- Train DataLoader
- Validation DataLoader
- Test DataLoader
- Class Mapping
- Batch Tensors
- Dataset Statistics

---

# R. Industry Best Practices

- Keep train, validation and test separate
- Augment training data only
- Normalize all inputs
- Use fixed image size
- Shuffle training data
- Validate dataset before training

---

# S. Common Mistakes

- Applying augmentation to test data
- Using different preprocessing across splits
- Forgetting normalization
- Mixing train and validation images
- Incorrect label mapping

---

# T. Deliverables

- Data Pipeline Design
- Augmentation Plan
- Batch Processing Strategy
- Data Loader Workflow
- Tensor Conversion Workflow
- Validation Strategy

---

# U. Pre-Requisites Before Next Step

✓ Dataset Verified

✓ Dataset Structure Finalized

✓ Technology Stack Finalized

✓ CNN Architecture Finalized

✓ Training Strategy Finalized

✓ Evaluation Strategy Finalized

---

# Summary

The data pipeline converts raw crop images into training-ready tensors through:

Load Image
    ↓
Resize
    ↓
Augmentation
    ↓
Normalization
    ↓
Tensor Conversion
    ↓
Batch Creation

This pipeline ensures consistency, robustness, and efficient CNN training.

---