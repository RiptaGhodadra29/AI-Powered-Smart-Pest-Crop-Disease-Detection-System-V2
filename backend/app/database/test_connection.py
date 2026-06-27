from sqlalchemy import text

from backend.app.database.database import engine


try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT 1")
        )

        print("Database Connected Successfully")

except Exception as e:
    print(f"Connection Failed: {e}")