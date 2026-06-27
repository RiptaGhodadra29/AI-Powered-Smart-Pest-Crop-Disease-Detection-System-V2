# AI-Powered Smart Pest & Crop Disease Detection System

# Backend API Documentation

Base URL:

http://127.0.0.1:8000

---

# 1. Health Check API

## Endpoint

GET /

## Description

Checks whether backend server is running.

## Response

```json
{
  "message": "Backend Running Successfully"
}
```

---

# 2. User Registration API

## Endpoint

POST /auth/register

## Request

```json
{
  "username": "ripta",
  "email": "ripta@example.com",
  "password": "password123"
}
```

## Response

```json
{
  "id": 1,
  "username": "ripta",
  "email": "ripta@example.com"
}
```

---

# 3. Image Upload API

## Endpoint

POST /images/upload

## Form Data

| Field | Type |
|---------|---------|
| user_id | integer |
| file | image |

## Response

```json
{
  "id": 1,
  "filename": "leaf.jpg",
  "filepath": "backend/uploads/leaf.jpg"
}
```

---

# 4. Disease Prediction API

## Endpoint

POST /predict

## Request

```json
{
  "user_id": 1,
  "image_id": 1
}
```

## Response

```json
{
  "prediction_id": 1,
  "class_name": "Tomato_Leaf_Mold",
  "confidence": 95.27,
  "model_name": "EfficientNet-B0",
  "recommendation": {
    "disease_name": "Tomato Leaf Mold",
    "severity": "Medium",
    "description": "Tomato Leaf Mold is a fungal disease common in humid environments especially greenhouses",
    "treatment": "Improve ventilation and apply fungicides if necessary",
    "organic_treatment": [
      "Neem oil spray",
      "Remove infected leaves"
    ],
    "chemical_treatment": [
      "Chlorothalonil",
      "Copper fungicides"
    ],
    "preventive_measures": [
      "Reduce humidity",
      "Increase plant spacing",
      "Improve airflow"
    ],
    "monitoring_actions": [
      "Inspect greenhouse crops regularly",
      "Remove infected foliage"
    ]
  }
}
```

---

# 5. Prediction History API

## Endpoint

GET /history/{user_id}

## Example

GET /history/1

## Response

```json
{
  "history": [
    {
      "prediction_id": 1,
      "class_name": "Corn Gray Leaf Spot",
      "confidence": 92.22,
      "model_name": "EfficientNet-B0"
    },
    {
      "prediction_id": 2,
      "class_name": "Tomato_Leaf_Mold",
      "confidence": 95.27,
      "model_name": "EfficientNet-B0"
    }
  ]
}
```

---

# 6. Dashboard API

## Endpoint

GET /dashboard/{user_id}

## Example

GET /dashboard/1

## Response

```json
{
  "user_id": 1,
  "total_predictions": 3,
  "most_detected_disease": "Tomato_Leaf_Mold",
  "average_confidence": 94.25
}
```

---

# Backend Technologies

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- PyTorch
- EfficientNet-B0

---

# Implemented Features

- User Registration
- Image Upload
- Disease Prediction
- Recommendation Engine
- Prediction History
- Dashboard Analytics
- Database Storage
- API Testing
- Swagger Documentation

---

# Swagger UI

Available at:

http://127.0.0.1:8000/docs

---

# ReDoc

Available at:

http://127.0.0.1:8000/redoc