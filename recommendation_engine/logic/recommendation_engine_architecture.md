# Recommendation Engine Architecture

## System Components

### Input Layer

Receives:

- Disease Predictions
- Pest Predictions

Examples:

Disease = Tomato Late Blight
Confidence = 0.94

Pest = Caterpillar
Confidence = 0.89

---

## Validation Layer

Responsibilities:

- Verify prediction exists
- Verify confidence threshold
- Verify knowledge base entry exists

---

## Knowledge Retrieval Layer

Disease Path:

Prediction
    ↓
Disease Knowledge Base Lookup
    ↓
Disease Record Retrieval

Pest Path:

Prediction
    ↓
Pest Knowledge Base Lookup
    ↓
Pest Record Retrieval

---

## Recommendation Generation Layer

Generates:

- Problem Name
- Severity
- Organic Recommendation
- Chemical Recommendation
- Prevention Measures
- Monitoring Advice

---

## Output Layer

Returns farmer-friendly recommendation.

Example:

Disease Detected:
Tomato Late Blight

Recommended Action:
Apply recommended fungicide.

Organic Option:
Copper-based spray.

Prevention:
Avoid prolonged leaf wetness.

Monitoring:
Inspect plants every week.