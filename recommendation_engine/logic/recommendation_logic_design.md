# Recommendation Logic Design

## Objective

Convert AI model predictions into actionable farmer recommendations.

---

## Input Sources

### Disease Classification Module

Output Example:

Disease = Tomato Late Blight
Confidence = 0.94

### Pest Detection Module

Output Example:

Pest = Caterpillar
Confidence = 0.89

---

## Recommendation Flow

Prediction
    ↓
Prediction Validation
    ↓
Knowledge Base Lookup
    ↓
Recommendation Retrieval
    ↓
Farmer Message Generation
    ↓
Output Display

---

## Disease Recommendation Workflow

Predicted Disease
        ↓
Find Disease ID
        ↓
Retrieve Disease Record
        ↓
Retrieve:
    - Symptoms
    - Treatment
    - Organic Treatment
    - Chemical Treatment
    - Prevention
    - Monitoring
        ↓
Generate Farmer Recommendation

---

## Pest Recommendation Workflow

Detected Pest
        ↓
Find Pest ID
        ↓
Retrieve Pest Record
        ↓
Retrieve:
    - Organic Control
    - Chemical Control
    - Prevention
    - Monitoring
        ↓
Generate Farmer Recommendation

---

## Confidence Handling

If confidence >= threshold:

    Show recommendation

Else:

    Ask farmer to upload a clearer image

---

## Future Enhancements

- Multi-disease recommendations
- Multiple pest recommendations
- Weather-aware recommendations
- Location-based recommendations
- Personalized recommendations