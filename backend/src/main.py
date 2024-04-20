from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .query import query_router
from .conversation import conversation_router
from loguru import logger

logger.add("./logs/{time}.log", level="TRACE", rotation="12:00")

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to RAG Chat History"}

app.include_router(query_router)
app.include_router(conversation_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)