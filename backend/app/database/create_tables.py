from backend.app.database.base import Base
from backend.app.database.database import engine

from backend.app.models import User
from backend.app.models import UploadedImage
from backend.app.models import Prediction
from backend.app.models import Recommendation


def create_tables():

    Base.metadata.create_all(bind=engine)

    print("Tables Created Successfully")


if __name__ == "__main__":
    create_tables()