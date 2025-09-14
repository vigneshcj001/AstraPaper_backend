from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

class Settings:
    OLLAMA_API: str = os.getenv("OLLAMA_API")
    MONGO_URI: str = os.getenv("MONGO_URI")
    DB_NAME: str = os.getenv("DB_NAME", "AstraPaper")

settings = Settings()
