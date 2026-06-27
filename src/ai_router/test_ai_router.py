from src.ai_router.ai_router import (
    AIRouter
)

router = AIRouter()

print("\n========== DISEASE TEST ==========\n")

disease_result = (
    router.predict_disease(
        "dataset/final_dataset/test/Tomato_healthy/efe6c986-b85c-40f1-8cb5-345acbb36b71___RS_HL 0579.JPG"
    )
)

print(disease_result)

print("\n========== PEST TEST ==========\n")

pest_result = (
    router.predict_pest(
        "dataset/raw/agripest/test/images/Weevil-237-_jpg.rf.9dfe41f1c17cfbbbb48c432ddd1c91b7.jpg"
    )
)

print(pest_result)