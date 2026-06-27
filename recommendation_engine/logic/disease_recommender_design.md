# Disease Recommender Design

## Purpose

Retrieve disease recommendation information from the Disease Knowledge Base.

---

## Input

Disease Name

Example:

Tomato Late Blight

---

## Processing

1. Load Disease Knowledge Base
2. Search Disease Name
3. Retrieve Matching Record
4. Return Recommendation Data

---

## Output

Disease Record

Fields:

- Disease Name
- Severity
- Description
- Symptoms
- Treatment
- Organic Treatment
- Chemical Treatment
- Prevention
- Monitoring

---

## Error Handling

If disease not found:

Return:
Disease recommendation not found.