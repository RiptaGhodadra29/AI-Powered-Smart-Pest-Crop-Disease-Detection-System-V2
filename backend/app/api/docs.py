from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def api_documentation():

    return {
        "project": "AI-Powered Smart Pest & Crop Disease Detection System",
        "version": "1.0",

        "available_apis": [

            {
                "name": "Authentication API",
                "endpoint": "/auth/register",
                "method": "POST"
            },

            {
                "name": "Image Upload API",
                "endpoint": "/images/upload",
                "method": "POST"
            },

            {
                "name": "Prediction API",
                "endpoint": "/prediction",
                "method": "POST"
            },

            {
                "name": "History API",
                "endpoint": "/history/{user_id}",
                "method": "GET"
            },

            {
                "name": "Dashboard API",
                "endpoint": "/dashboard/{user_id}",
                "method": "GET"
            }
        ]
    }