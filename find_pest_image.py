from ultralytics import YOLO
import os

# Load your trained pest model
model = YOLO(
    "runs/detect/experiments/pest_detection/yolo11s_640_100e_bs8_v1-2/weights/best.pt"
)

image_dir = "dataset/raw/agripest/test/images"

found = False

for image_name in os.listdir(image_dir):

    image_path = os.path.join(
        image_dir,
        image_name
    )

    try:
        results = model(image_path)

        if len(results[0].boxes) > 0:

            print("\nPest detected!")
            print("Image:", image_name)

            for box in results[0].boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                print(
                    f"Class: {model.names[class_id]}"
                )

                print(
                    f"Confidence: {confidence:.2%}"
                )

            found = True
            break

    except Exception as e:
        print(
            f"Error processing {image_name}: {e}"
        )

if not found:
    print(
        "\nNo pest detections found in test/images folder."
    )