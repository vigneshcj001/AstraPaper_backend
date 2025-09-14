from pydantic import BaseModel
from datetime import datetime

class QuerySchema(BaseModel):
    user_id: str
    query_type: str
    input_text: str
    output_text: str
    created_at: datetime = datetime.utcnow()