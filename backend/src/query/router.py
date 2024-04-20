from ..database import get_db
from fastapi import APIRouter, Depends
from .utils import engine
from .schema import Query

query_router = APIRouter(
  prefix='/query',
  tags=['Query the vector db']
)

@query_router.post("/chat")
async def query(query_payload: Query,db = Depends(get_db)):
    return engine(query_payload.query, query_payload.conversation_id, db)
