from ..config import settings
from llama_index.core import StorageContext,VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from llama_index.vector_stores.lancedb import LanceDBVectorStore
from llama_index.llms.openai import OpenAI
from llama_index.core.base.llms.types import ChatMessage,MessageRole
from ..conversation.crud import create_conversation,create_message,fetch_messages
from sqlalchemy.orm import Session
from typing import List
from loguru import logger

Settings.embed_model = OpenAIEmbedding(model=settings.EMBEDDING_MODEL ,api_key=settings.OPENAI_KEY)
Settings.llm = OpenAI(temperature=0.1,api_key= settings.OPENAI_KEY)
vector_store = LanceDBVectorStore(uri=settings.VECTOR_URI)

def get_chat_history(
    chat_messages:List[dict],
) -> List[ChatMessage]:
  
    chat_history = []
    for message in chat_messages:
        chat_history.append(ChatMessage(content=message['content'], role=message['role']))
    return chat_history[-4:]


storage_context = StorageContext.from_defaults(
            vector_store=vector_store
        )

index = VectorStoreIndex.from_documents(
    documents=[], storage_context=storage_context
)

chat_engine = index.as_chat_engine(
    chat_mode="context",
    system_prompt=(
       "You are a helpful AI assistant that can answer questions about the Harry Potter movie series. "
        "You have access to a knowledge base about the movies' plots, including information about characters, "
    ),
)


def engine(query,conersation_id,db: Session):
    logger.debug(f"Received query: {query} and conversation_id: {conersation_id}")
    chat_history = []
    if not(conersation_id):
        conversation_id = create_conversation(db=db,name=query[:20])
    else:
        conversation_id = conersation_id
        messages = fetch_messages(db=db, conversation_id=conversation_id)
        chat_history.extend(get_chat_history(chat_messages=messages))
    
    logger.debug(f"Chat history: {chat_history}")
    create_message(db=db, conversation_id=conversation_id, content=query, role=MessageRole.USER)
    response = chat_engine.chat(query, chat_history=chat_history)
    create_message(db=db, conversation_id=conversation_id, content=response.response, role=MessageRole.ASSISTANT)
    logger.info(f"Query response: {response.response} and conversation_id: {conversation_id}")
    return {
        "response": response.response,
        "conversation_id": conversation_id
    }