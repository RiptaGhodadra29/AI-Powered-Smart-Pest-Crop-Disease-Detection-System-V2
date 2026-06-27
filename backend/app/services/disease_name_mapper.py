DISEASE_NAME_MAPPING = {

    # Apple
    "Apple_Rust": "Apple Rust",
    "Apple_Scab": "Apple Scab",
    "Apple_healthy": "Apple Healthy",

    # Blueberry
    "Blueberry_healthy": "Blueberry Healthy",

    # Cherry
    "Cherry_healthy": "Cherry Healthy",

    # Corn
    "Corn_Blight": "Corn Leaf Blight",
    "Corn_Gray_Leaf_Spot": "Corn Gray Leaf Spot",
    "Corn_Rust": "Corn Rust",

    # Grape
    "Grape_Black_Rot": "Grape Black Rot",
    "Grape_healthy": "Grape Healthy",

    # Peach
    "Peach_healthy": "Peach Healthy",

    # Pepper
    "Pepper__bell___Bacterial_spot":
        "Pepper Bell Bacterial Spot",

    "Pepper__bell___healthy":
        "Pepper Healthy",

    # Potato
    "Potato___Early_blight":
        "Potato Early Blight",

    "Potato___Late_blight":
        "Potato Late Blight",

    "Potato___healthy":
        "Potato Healthy",

    # Raspberry
    "Raspberry_healthy":
        "Raspberry Healthy",

    # Rice
    "Rice_Bacterial_Blight":
        "Rice Bacterial Blight",

    "Rice_Blast":
        "Rice Blast",

    "Rice_Brown_Spot":
        "Rice Brown Spot",

    "Rice_Tungro":
        "Rice Tungro",

    # Soybean
    "Soybean_healthy":
        "Soybean Healthy",

    # Strawberry
    "Strawberry_healthy":
        "Strawberry Healthy",

    # Tomato
    "Tomato_Bacterial_spot":
        "Tomato Bacterial Spot",

    "Tomato_Early_blight":
        "Tomato Early Blight",

    "Tomato_Late_blight":
        "Tomato Late Blight",

    "Tomato_Leaf_Mold":
        "Tomato Leaf Mold",

    "Tomato_Septoria_leaf_spot":
        "Tomato Septoria Leaf Spot",

    "Tomato_Spider_mites_Two_spotted_spider_mite":
        "Tomato Spider Mites",

    "Tomato__Target_Spot":
        "Tomato Target Spot",

    "Tomato__Tomato_YellowLeaf__Curl_Virus":
        "Tomato Yellow Leaf Curl Virus",

    "Tomato__Tomato_mosaic_virus":
        "Tomato Mosaic Virus",

    "Tomato_healthy":
        "Tomato Healthy"
}


def map_disease_name(predicted_name: str):
    return DISEASE_NAME_MAPPING.get(
        predicted_name,
        predicted_name
    )