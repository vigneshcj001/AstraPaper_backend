import os
from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import extract_text_from_pdf
from app.models.response_models import AIResponse

router = APIRouter(prefix="/upload", tags=["upload"])

# Define temp folder path
TEMP_DIR = "temp_"

# Make sure folder exists
os.makedirs(TEMP_DIR, exist_ok=True)

@router.post("/", response_model=AIResponse)
async def upload_pdf(file: UploadFile = File(...)):
    # Save file inside temp_ directory
    file_path = os.path.join(TEMP_DIR, file.filename)
    
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    # Extract text
    text = extract_text_from_pdf(file_path)

    return AIResponse(output=text[:500])
