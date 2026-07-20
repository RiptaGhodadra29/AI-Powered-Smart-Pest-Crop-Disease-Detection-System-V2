DISEASE_NAME_MAPPING = {

    # Apple
    "Apple_Rust": "Apple Rust",
    "Apple_Scab": "Apple Scab",
    "Apple_healthy": "Apple Healthy",

    # Banana
    "Banana_Black_Sigatoka": "Banana Black Sigatoka",
    "Banana_Bract_Mosaic_Virus": "Banana Bract Mosaic Virus",
    "Banana_Moko_Disease": "Banana Moko Disease",
    "Banana_Panama_Disease": "Banana Panama Disease",
    "Banana_Yellow_Sigatoka": "Banana Yellow Sigatoka",
    "Banana_healthy": "Banana Healthy",

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

    # Groundnut
    "Groundnut_Nutrition_Deficiency":
        "Groundnut Nutrition Deficiency",

    "Groundnut_Rust":
        "Groundnut Rust",

    "Groundnut_Tikka_Leaf_Spot":
        "Groundnut Tikka Leaf Spot",

    "Groundnut_healthy":
        "Groundnut Healthy",

    # Mango
    "Mango_Anthracnose":
        "Mango Anthracnose",

    "Mango_Bacterial_Canker":
        "Mango Bacterial Canker",

    "Mango_Cutting_Weevil":
        "Mango Cutting Weevil",

    "Mango_Die_Back":
        "Mango Die Back",

    "Mango_Gall_Midge":
        "Mango Gall Midge",

    "Mango_Powdery_Mildew":
        "Mango Powdery Mildew",

    "Mango_Sooty_Mould":
        "Mango Sooty Mould",

    "Mango_healthy":
        "Mango Healthy",

    # Peach
    "Peach_healthy":
        "Peach Healthy",

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

    # Sugarcane
    "Sugarcane_Red_Rot":
        "Sugarcane Red Rot",

    "Sugarcane_Rust":
        "Sugarcane Rust",

    "Sugarcane_Smut":
        "Sugarcane Smut",

    "Sugarcane_healthy":
        "Sugarcane Healthy",

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
        "Tomato Healthy",

    # Wheat
    "Wheat_Brown_Rust":
        "Wheat Brown Rust",

    "Wheat_Powdery_Mildew":
        "Wheat Powdery Mildew",

    "Wheat_Yellow_Rust":
        "Wheat Yellow Rust",

    "Wheat_healthy":
        "Wheat Healthy",

    # Special
    "Unknown_Crop":
        "Unknown Crop"
}


def map_disease_name(predicted_name: str):
    return DISEASE_NAME_MAPPING.get(
        predicted_name,
        predicted_name
    )