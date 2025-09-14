from fastapi import APIRouter
from app.models.request_models import CritiqueRequest
from app.models.response_models import AIResponse
from app.services.ollama_service import run_ollama

router = APIRouter(prefix="/critique", tags=["critique"])
@router.post("/", response_model=AIResponse)
async def critique_answer(request: CritiqueRequest):
    result = await run_ollama("deepseek-r1:1.5b", f"Critically review this answer: {request.answer} and improve it if necessary.")
    return AIResponse(output=result)