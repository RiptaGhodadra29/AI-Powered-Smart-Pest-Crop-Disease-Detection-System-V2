DISEASE_CLASS_MAPPING = {

"Apple_Rust": "Apple Rust",
"Apple_Scab": "Apple Scab",

"Corn_Blight": "Corn Leaf Blight",
"Corn_Gray_Leaf_Spot": "Corn Gray Leaf Spot",
"Corn_Rust": "Corn Rust",

"Grape_Black_Rot": "Grape Black Rot",

"Pepper__bell___Bacterial_spot":
    "Pepper Bell Bacterial Spot",

"Potato___Early_blight":
    "Potato Early Blight",

"Potato___Late_blight":
    "Potato Late Blight",

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

"Rice_Bacterial_Blight":
    "Rice Bacterial Blight",

"Rice_Blast":
    "Rice Blast",

"Rice_Brown_Spot":
    "Rice Brown Spot",

"Rice_Tungro":
    "Rice Tungro",
}

def map_disease_name(class_name):
    """
    Convert model output class name
    into knowledge base disease name.
    """

    return DISEASE_CLASS_MAPPING.get(class_name)