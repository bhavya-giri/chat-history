from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class Query(BaseModel):
    query: str
    conversation_id: Optional[UUID] = None
