from fastapi import FastAPI

# Routers
from backend.app.api.auth import router as auth_router
from backend.app.api.image import router as image_router
from backend.app.api.prediction import router as prediction_router
from backend.app.api.history import router as history_router
from backend.app.api.dashboard import router as dashboard_router
from backend.app.api.docs import router as docs_router
from backend.app.api import pest_detection
from backend.app.api.ai_router import (router as ai_router_router)


# Core setup
from backend.app.core.cors import setup_cors


app = FastAPI(
    title="AI-Powered Smart Pest & Crop Disease Detection System",
    description="Backend API for crop disease detection, pest detection and recommendations",
    version="1.0.0"
)


# Setup CORS
setup_cors(app)


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "AI Crop Disease Detection API is running 🚀"
    }


# Authentication APIs
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)


# Image Upload APIs
app.include_router(
    image_router,
    prefix="/image",
    tags=["Image Upload"]
)


# Prediction APIs
app.include_router(
    prediction_router,
    prefix="/predict",
    tags=["Prediction"]
)
app.include_router(
    pest_detection.router,
    prefix="/detect",
    tags=["Pest Detection"]
)

app.include_router(
    history_router,
    prefix="/history",
    tags=["History"]
)


app.include_router(
    dashboard_router,
    prefix="/dashboard",
    tags=["Dashboard"]
)

app.include_router(
    docs_router,
    prefix="/docs-api",
    tags=["Documentation"]
)

app.include_router(
    ai_router_router,
    prefix="/router",
    tags=["AI Router"]
)