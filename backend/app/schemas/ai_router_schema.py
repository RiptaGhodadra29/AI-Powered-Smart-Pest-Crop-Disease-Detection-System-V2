from pydantic import BaseModel


class AIRouterRequest(BaseModel):

    user_id: int
    image_id: int

    # manual router for now
    image_type: str
    language: str = "en"


class AIRouterResponse(BaseModel):

    prediction_type: str

    result: dict