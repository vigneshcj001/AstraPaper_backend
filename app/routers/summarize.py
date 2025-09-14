from fastapi import APIRouter
from app.models.response_models import AIResponse
from app.models.request_models import SummarizationRequest
from app.services.ollama_service import run_ollama

router = APIRouter(prefix="/summarize", tags=["summarize"])

@router.post("/", response_model=AIResponse)
async def summarize_text(request: SummarizationRequest):    
    result = await run_ollama("deepseek-r1:1.5b", f"Summarize the following text:\n{request.text}")
    return AIResponse(output=result)