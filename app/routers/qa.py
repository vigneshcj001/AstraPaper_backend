from fastapi import APIRouter
from app.models.request_models import QARequest
from app.models.response_models import AIResponse
from app.services.fusion_service import fuse_responses

router = APIRouter(prefix="/qa", tags=["qa"])

@router.post("/", response_model=AIResponse)
async def qa(request: QARequest):
    result = await fuse_responses(request.question, request.context)
    return AIResponse(output=result)