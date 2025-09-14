import httpx
from app.core.config import settings
from app.core.utils import logger

async def run_ollama(model: str, prompt: str) -> str:
    url = f"{settings.OLLAMA_API}/api/generate"
    payload = {"model": model, "prompt": prompt}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Model: {model} response: {data}")
        return data.get("response", "")