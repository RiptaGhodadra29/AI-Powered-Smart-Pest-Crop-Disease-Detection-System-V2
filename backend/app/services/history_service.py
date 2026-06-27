from backend.app.models.prediction import Prediction


def get_user_history(
    db,
    user_id
):
    return (
        db.query(Prediction)
        .filter(
            Prediction.user_id == user_id
        )
        .all()
    )