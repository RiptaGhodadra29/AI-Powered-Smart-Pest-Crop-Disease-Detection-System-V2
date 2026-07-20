from backend.app.services.prediction_service import (
    create_prediction
)

from backend.app.services.pest_detection_service import (
    detect_and_save_pests
)

from backend.app.models.uploaded_image import (
    UploadedImage
)

from backend.app.services.farmer_response_service import (
    FarmerResponseService
)


class AIRouterService:

    def route_image(
        self,
        db,
        user_id,
        image_id,
        image_type,
        language="en"
    ):

        image = (
            db.query(UploadedImage)
            .filter(
                UploadedImage.id == image_id
            )
            .first()
        )

        if not image:
            return None

        image_type = image_type.lower()

        # Disease Route
        if image_type == "disease":

            result = create_prediction(
                db=db,
                user_id=user_id,
                image_id=image_id,
                language=language
            )

            return (
                FarmerResponseService
                .format_disease_response(
                    result
                )
            )

        # Pest Route
        elif image_type == "pest":

            result = detect_and_save_pests(
                db=db,
                user_id=user_id,
                image_id=image_id,
                image_path=image.image_path
            )

            return (
                FarmerResponseService
                .format_pest_response(
                    result
                )
            )

        return {
            "error": "invalid image type"
        }