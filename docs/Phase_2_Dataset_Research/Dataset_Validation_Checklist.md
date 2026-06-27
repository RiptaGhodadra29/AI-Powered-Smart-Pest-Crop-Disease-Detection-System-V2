# Dataset Validation Checklist

## Project
AI-Powered Smart Pest & Crop Disease Detection System

## Purpose

This checklist is used to verify dataset quality before preprocessing, model training, and evaluation.

---

# 1. Dataset Structure Validation

## PlantVillage

- [ ] Dataset folder exists
- [ ] All class folders exist
- [ ] Images are accessible
- [ ] No empty folders

## PlantDoc

- [ ] Train folder exists
- [ ] Test folder exists
- [ ] All class folders exist
- [ ] Images are accessible

## IP102

- [ ] Images folder exists
- [ ] train.txt exists
- [ ] val.txt exists
- [ ] test.txt exists
- [ ] Images are accessible

---

# 2. Corrupted Image Check

Verify:

- [ ] Images open successfully
- [ ] No zero-byte images
- [ ] No unreadable images
- [ ] No unsupported image formats

Expected Output:

- Corrupted image count
- Corrupted image report

---

# 3. Duplicate Image Check

Verify:

- [ ] Exact duplicate images
- [ ] Duplicate filenames
- [ ] Duplicate records

Expected Output:

- Duplicate image count
- Duplicate image report

---

# 4. Missing Data Check

Verify:

- [ ] Missing images
- [ ] Missing labels
- [ ] Missing folders
- [ ] Missing metadata

Expected Output:

- Missing data report

---

# 5. Class Distribution Analysis

PlantVillage

- [ ] Count images per class
- [ ] Identify minority classes
- [ ] Identify majority classes

PlantDoc

- [ ] Count images per class
- [ ] Identify minority classes
- [ ] Identify majority classes

IP102

- [ ] Count images per pest class
- [ ] Identify minority classes
- [ ] Identify majority classes

Expected Output:

- Class distribution table
- Class distribution graph

---

# 6. Class Name Validation

Verify:

- [ ] No duplicate class names
- [ ] Standardized naming convention
- [ ] Class mapping verified

Expected Output:

- Updated Class_Mapping.csv

---

# 7. Train-Test Leakage Check

Verify:

- [ ] No duplicate images between train and test
- [ ] No duplicate images between train and validation
- [ ] No leakage across splits

Expected Output:

- Leakage report

---

# 8. Annotation Validation

Verify:

- [ ] Labels are valid
- [ ] Labels match image files
- [ ] Class IDs are correct
- [ ] No invalid annotations

Expected Output:

- Annotation validation report

---

# 9. Dataset Statistics

Generate:

- [ ] Total images
- [ ] Total classes
- [ ] Images per class
- [ ] Dataset size (GB)
- [ ] Average image resolution

Expected Output:

- Dataset statistics report

---

# 10. Dataset Readiness Review

Dataset is considered ready when:

- [ ] No corrupted images
- [ ] No missing files
- [ ] No train-test leakage
- [ ] Class mapping completed
- [ ] Dataset statistics generated
- [ ] Validation reports generated

Status:

Dataset Ready For Preprocessing:

- [ ] YES
- [ ] NO

---

# Validation Summary

Date:

Validator:

Remarks:

Dataset Approved For Phase 3:

- [ ] YES
- [ ] NO