import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AI-Research-Agent")

def clean_text(text: str) -> str:
    return " ".join(text.split())
