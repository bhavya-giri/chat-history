from ..database import get_db
from fastapi import APIRouter, Depends
from .crud import fetch_conversations,fetch_messages
import uuid

conversation_router = APIRouter(
  prefix='/conversation',
  tags=['Conversation APIs']
)

@conversation_router.get("/fetch")
async def get_conversations(db = Depends(get_db)):
    return fetch_conversations(db)

@conversation_router.get("/messages/")
async def get_messages(conversation_id: uuid.UUID, db = Depends(get_db)):
    return fetch_messages(db, str(conversation_id))