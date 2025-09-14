from pydantic import BaseModel

class SummarizationRequest(BaseModel):
    text: str

class CritiqueRequest(BaseModel):
    text: str
    
class QARequest(BaseModel):
    question: str
    context: str

class GenerateRequest(BaseModel):
    idea: str