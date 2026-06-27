# Recommendation Test Cases

## Disease Test Cases

### TC001

Input:
Tomato Late Blight

Expected:
Correct disease recommendation returned.

---

### TC002

Input:
Potato Early Blight

Expected:
Correct disease recommendation returned.

---

### TC003

Input:
Corn Rust

Expected:
Correct disease recommendation returned.

---

## Pest Test Cases

### TC004

Input:
Caterpillars

Expected:
Correct pest control recommendation returned.

---

### TC005

Input:
Grasshoppers

Expected:
Correct pest control recommendation returned.

---

### TC006

Input:
Weevils

Expected:
Correct pest control recommendation returned.

---

## Beneficial Organism Test Cases

### TC007

Input:
Bees

Expected:
Protection recommendation returned.

---

### TC008

Input:
Earthworms

Expected:
Soil health recommendation returned.

---

## Error Handling Test Cases

### TC009

Input:
Unknown Disease

Expected:
Recommendation not found message.

---

### TC010

Input:
Unknown Pest

Expected:
Recommendation not found message.

---

### TC011

Input:
Confidence < Threshold

Expected:
Request clearer image.