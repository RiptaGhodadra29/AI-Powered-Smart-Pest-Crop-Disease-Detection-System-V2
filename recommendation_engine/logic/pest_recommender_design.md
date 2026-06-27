# Pest Recommender Design

## Purpose

Retrieve pest recommendations from the Pest Knowledge Base.

## Input

Pest Name

Example:
Caterpillars

## Processing

1. Load Pest Knowledge Base
2. Search Pest Name
3. Retrieve Matching Record
4. Return Recommendation Data

## Output

Pest Record

Fields:

- Pest Name
- Severity
- Description
- Damage Symptoms
- Organic Control
- Chemical Control
- Preventive Measures
- Monitoring Actions

## Error Handling

If pest not found:

Return:
Pest recommendation not found.