from ultralytics import YOLO

from src.recommendation_engine.pest_recommender import (
    PestRecommender
)

from backend.app.models.prediction import (
    Prediction
)

# Load trained pest model
model = YOLO(
    "runs/detect/experiments/pest_detection/yolo11s_640_100e_bs8_v1-2/weights/best.pt"
)

pest_recommender = PestRecommender()


def detect_pests(image_path: str):

    results = model(image_path)

    detections = []

    for result in results:

        boxes = result.boxes

        if boxes is None:
            continue

        for box in boxes:

            class_id = int(
                box.cls[0].item()
            )

            confidence = round(
                float(box.conf[0].item()) * 100,
                2
            )

            if confidence < 50:
                continue

            pest_name = model.names[
                class_id
            ]

            recommendation = (
                pest_recommender.get_recommendation(
                    pest_name
                )
            )

            detections.append(
                {
                    "class_id": class_id,
                    "pest_name": pest_name,
                    "confidence": confidence,
                    "recommendation": recommendation
                }
            )

    return detections


def detect_and_save_pests(
    db,
    user_id,
    image_id,
    image_path
):

    detections = detect_pests(
        image_path
    )

    for pest in detections:

        prediction = Prediction(
            user_id=user_id,
            image_id=image_id,
            prediction_type="pest",
            model_name="YOLOv11",
            class_id=pest["class_id"],
            class_name=pest["pest_name"],
            confidence=pest["confidence"]
        )

        db.add(prediction)

    db.commit()

    return detections