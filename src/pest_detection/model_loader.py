from pathlib import Path
from ultralytics import YOLO


MODEL_PATH = (
    Path(__file__)
    .resolve()
    .parents[2]
    / "runs"
    / "detect"
    / "experiments"
    / "pest_detection"
    / "yolo11s_640_100e_bs8_v1-2"
    / "weights"
    / "best.pt"
)


def load_pest_model():
    return YOLO(str(MODEL_PATH))