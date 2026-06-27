from .knowledge_base_loader import KnowledgeBaseLoader
loader = KnowledgeBaseLoader()

disease_df = loader.load_disease_kb()
pest_df = loader.load_pest_kb()

print("\nDisease Records:")
print(len(disease_df))

print("\nPest Records:")
print(len(pest_df))