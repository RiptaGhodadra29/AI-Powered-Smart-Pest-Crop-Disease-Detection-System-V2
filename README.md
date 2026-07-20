# 🌱 AI-Powered Smart Pest & Crop Disease Detection System

An end-to-end AI-powered agricultural assistant that helps farmers detect crop diseases and pests from images and provides multilingual recommendations for treatment and prevention.

---

# 📌 Project Overview

This project combines:

- Computer Vision
- Deep Learning
- FastAPI Backend
- React Frontend
- PostgreSQL Database
- Gemini AI Recommendations

to build a smart farming solution capable of:

✅ Crop Disease Detection

✅ Pest Detection

✅ Multilingual Recommendations

✅ Farmer-Friendly Explanations

✅ Prediction History Tracking

✅ AI-Powered Treatment Suggestions

---

# 🎯 Problem Statement

Crop diseases and pest attacks cause significant yield losses worldwide.

Farmers often:

- Cannot identify diseases early
- Lack expert guidance
- Receive recommendations in languages they do not understand

This system provides instant disease and pest detection using AI and delivers treatment recommendations in multiple languages.

---

# 🚀 Key Features

## Disease Detection

Detects diseases from crop leaf images using EfficientNet-B0.

### Supported Disease Classes

- Tomato Diseases
- Potato Diseases
- Pepper Diseases
- Rice Diseases
- Wheat Diseases
- Sugarcane Diseases
- Mango Diseases
- Banana Diseases
- Groundnut Diseases
- Apple Diseases
- Corn Diseases
- Grape Diseases

and more.

---

## Pest Detection

Detects agricultural pests using YOLO.

### Supported Pest Classes

- Ants
- Bees
- Beetles
- Caterpillars
- Earthworms
- Earwigs
- Grasshoppers
- Moths
- Slugs
- Snails
- Wasps
- Weevils

---

## AI Recommendation Engine

Provides:

- Disease Description
- Severity Assessment
- Organic Treatment
- Chemical Treatment
- Preventive Measures
- Monitoring Actions

Powered by:

- Knowledge Base
- Gemini AI

---

## Multilingual Support

Recommendations available in:

- English
- Gujarati
- Hindi

---

## User Features

- User Registration
- Login Authentication
- Image Upload
- Prediction History
- Recommendation Dashboard

---

# 🏗 System Architecture

```text
Farmer
   │
   ▼
React Frontend
   │
   ▼
FastAPI Backend
   │
   ├── Disease Model (EfficientNet-B0)
   │
   ├── Pest Model (YOLO)
   │
   ├── Gemini Recommendation Engine
   │
   └── PostgreSQL Database
```

---

# 🧠 AI Models

## Disease Classification Model

| Property | Value |
|-----------|--------|
| Model | EfficientNet-B0 |
| Framework | PyTorch |
| Classes | 60 |
| Validation Accuracy | ~95% |

---

## Pest Detection Model

| Property | Value |
|-----------|--------|
| Model | YOLO |
| Framework | Ultralytics |
| Pest Classes | 12 |

---

# 📂 Dataset

Dataset Version:

```text
dataset/final_dataset_v2
```

Contains:

```text
Train
Validation
Test
Unknown Crop Dataset
```

### Total Classes

60 Disease Classes

### Total Images

66,354 Images

For detailed dataset information:

- docs/DATASET_SOURCES.md
- docs/DATASET_STRUCTURE.md
- docs/CLASS_DISTRIBUTION.md

---

# 🛠 Technology Stack

## Frontend

- React
- Vite
- Tailwind CSS
- React Router

## Backend

- FastAPI
- SQLAlchemy
- JWT Authentication

## Database

- PostgreSQL

## AI/ML

- PyTorch
- EfficientNet-B0
- YOLO
- Gemini AI

---

# 📁 Project Structure

```text
AI_Powered_Smart_Pest_Crop_Disease_Detection_System
│
├── backend
│
├── frontend
│
├── src
│   ├── training
│   ├── inference
│   ├── recommendation_engine
│   └── evaluation
│
├── dataset
│
├── artifacts
│
├── docs
│
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/RiptaGhodadra29/AI-Powered-Smart-Pest-Crop-Disease-Detection-System-V2.git
```

```bash
cd AI-Powered-Smart-Pest-Crop-Disease-Detection-System-V2
```

---

## Backend Setup

```bash
cd backend
```

```bash
pip install -r requirements.txt
```

```bash
uvicorn main:app --reload
```

---

## Frontend Setup

```bash
cd frontend
```

```bash
npm install
```

```bash
npm run dev
```

---

# 📡 API Endpoints

## Authentication

```http
POST /auth/register
POST /auth/login
```

## Prediction

```http
POST /router/predict
```

## Recommendations

```http
POST /recommendation/regenerate
```

## History

```http
GET /history
```

---

# 📈 Results

## Disease Classification

Validation Accuracy:

```text
≈ 95%
```

## Pest Detection

YOLO-based object detection for agricultural pests.

---

# 🔮 Future Enhancements

- Severity Detection Module
- Voice Assistant
- Weather Integration
- Notification System
- Mobile Application
- Intelligent AI Router
- Real-Time Camera Detection

---

# 👨‍💻 Developer

**Ripta Ghodadra**

Computer Engineering Student

AI / Machine Learning Enthusiast

GitHub:
https://github.com/RiptaGhodadra29

---

# 📜 License

This project is developed for educational, research, and academic purposes.
