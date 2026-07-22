from fastapi import FastAPI

# Routers
from app.api.auth import router as auth_router
from app.api.image import router as image_router
from app.api.prediction import router as prediction_router
from app.api.history import router as history_router
from app.api.dashboard import router as dashboard_router
from app.api.docs import router as docs_router
from app.api import pest_detection
from app.api.ai_router import (router as ai_router_router)
from app.api.recommendation import (router as recommendation_router)



# Core setup
from app.core.cors import setup_cors


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
    recommendation_router,
    prefix="/recommendation",
    tags=["Recommendation"]
)

app.include_router(
    ai_router_router,
    prefix="/router",
    tags=["AI Router"]
)

