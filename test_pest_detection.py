from backend.app.services.pest_detection_service import (
    detect_pests
)

result = detect_pests(
    "backend/uploads/images/005a6243-f1ea-4ed3-90fc-20735d067ce0.JPG"
)

print(result)