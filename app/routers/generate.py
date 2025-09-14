from fastapi import APIRouter
from app.models.request_models import GenerateRequest
from app.models.response_models import AIResponse
from app.services.ollama_service import run_ollama

router = APIRouter(prefix="/generate", tags=["generate"])   

@router.post("/", response_model=AIResponse)
async def generate_text(request: GenerateRequest):
    result = await run_ollama("qwen3:4b", f"Generate a detailed response based on the following prompt:\n{request.idea}")
    return AIResponse(output=result)