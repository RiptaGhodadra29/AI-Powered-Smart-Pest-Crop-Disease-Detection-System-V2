# Recommendation Service Design

## Purpose

Acts as the central controller of the recommendation engine.

---

## Inputs

Prediction Type:
- Disease
- Pest

Prediction Name:
- Tomato Late Blight
- Caterpillars
- etc.

---

## Processing

1. Receive prediction
2. Identify prediction type
3. Route to appropriate recommender
4. Retrieve recommendation record
5. Generate farmer-friendly message
6. Return final recommendation

---

## Outputs

Farmer-readable recommendation

---

## Error Handling

Unknown disease:
Return recommendation unavailable message

Unknown pest:
Return recommendation unavailable message

Low confidence:
Request clearer image
