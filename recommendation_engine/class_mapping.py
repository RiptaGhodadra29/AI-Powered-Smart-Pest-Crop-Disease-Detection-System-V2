"""
Maps model class names
to knowledge base disease names.
"""

DISEASE_CLASS_MAPPING = {

    # Apple
    "Apple_Rust": "Apple Rust",
    "Apple_Scab": "Apple Scab",

    # Corn
    "Corn_Blight": "Corn Leaf Blight",
    "Corn_Gray_Leaf_Spot": "Corn Gray Leaf Spot",
    "Corn_Rust": "Corn Rust",

    # Grape
    "Grape_Black_Rot": "Grape Black Rot",

    # Pepper
    "Pepper__bell___Bacterial_spot":
        "Pepper Bell Bacterial Spot",

    # Potato
    "Potato___Early_blight":
        "Potato Early Blight",

    "Potato___Late_blight":
        "Potato Late Blight",

    # Rice
    "Rice_Bacterial_Blight":
        "Rice Bacterial Blight",

    "Rice_Blast":
        "Rice Blast",

    "Rice_Brown_Spot":
        "Rice Brown Spot",

    "Rice_Tungro":
        "Rice Tungro",

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
}


def map_disease_name(class_name):
    """
    Convert model output class name
    into disease knowledge base name.
    """

    return DISEASE_CLASS_MAPPING.get(class_name)