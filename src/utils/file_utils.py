import os

def create_project_dirs():
    os.makedirs("artifacts/models", exist_ok=True)
    os.makedirs("artifacts/logs", exist_ok=True)