# Disease Knowledge Base Schema

## Purpose

This schema defines the standard structure for storing crop disease information in the Disease Knowledge Base.

The Recommendation Engine will use this information to generate farmer-friendly recommendations.

---

# Disease Record Structure

## 1. Disease Information

### disease_id
Unique disease identifier.

Example:
DIS001

---

### disease_name

Disease name predicted by the classification model.

Example:
Tomato Early Blight

---

### crop_name

Crop affected by the disease.

Example:
Tomato

---

### scientific_name

Scientific name of the pathogen.

Example:
Alternaria solani

---

### disease_type

Disease category.

Possible Values:

- Fungal
- Bacterial
- Viral
- Pest Related
- Nutrient Deficiency

---

### description

Simple explanation of the disease.

Example:

Early Blight is a fungal disease that affects tomato leaves, stems, and fruits.

---

## 2. Symptom Information

### symptoms

Visible symptoms observed on plants.

Examples:

- Brown circular spots
- Yellowing leaves
- Wilting

---

### affected_parts

Plant parts affected.

Possible Values:

- Leaf
- Stem
- Fruit
- Root
- Entire Plant

---

## 3. Cause Information

### cause

Primary reason for disease occurrence.

Example:

Alternaria solani fungus infection.

---

### favorable_conditions

Environmental conditions that support disease development.

Examples:

- High humidity
- Warm temperature
- Wet foliage

---

## 4. Severity Information

### severity_level

Possible Values:

- Low
- Medium
- High
- Critical

---

### yield_impact

Expected crop loss.

Example:

20–50% yield reduction.

---

## 5. Treatment Information

### treatment

Recommended treatment approach.

---

### organic_treatment

Organic treatment options.

Example:

Neem oil spray.

---

### chemical_treatment

Recommended chemical treatment.

Example:

Mancozeb fungicide.

---

### application_instructions

Instructions for applying treatment.

Example:

Apply every 7–10 days.

---

## 6. Prevention Information

### preventive_measures

Preventive actions.

Examples:

- Crop rotation
- Field sanitation
- Healthy seedlings

---

### monitoring_actions

Monitoring recommendations.

Examples:

- Weekly inspection
- Remove infected leaves

---

## 7. References

### references

Trusted information sources.

Examples:

- Agricultural Universities
- Government Agriculture Departments
- Research Publications

---

# Validation Rules

1. Every disease must have a unique disease_id.
2. Every disease must contain symptoms.
3. Every disease must contain treatment recommendations.
4. Every disease must contain prevention recommendations.
5. Every disease must contain monitoring actions.
6. Every disease must contain at least one verified source.
7. Recommendations must be farmer-friendly.