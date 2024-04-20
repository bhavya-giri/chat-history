from sqlalchemy.orm import Session
from ..models import Conversation,Message
from sqlalchemy import desc
from fastapi import HTTPException
from datetime import datetime
from loguru import logger

def fetch_conversations(db: Session):
    logger.debug("Fetching conversations")
    try:
        conversations = (
            db.query(Conversation)
            .order_by(desc(Conversation.dateCreated))
            .all()
        )
        if conversations:
            logger.info(f"Fetched {len(conversations)} conversations")
            return [
            {"id": conversation.id, "name": conversation.name}
            for conversation in conversations
            ]
        else:
            logger.info("No conversations found")
            return []
    except Exception as e:
        logger.error(f"Error fetching conversations: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
def fetch_messages(db: Session, conversation_id: str):
    logger.debug(f"Fetching messages for conversation {conversation_id}")
    try:
        messages = (
            db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .all()
        )
        if messages:
            logger.info(f"Fetched {len(messages)} messages for conversation {conversation_id}")
            return [
                {"role": message.role, "content": message.content}
                for message in messages
            ]
        else:
            logger.info(f"No messages found for conversation {conversation_id}")
            return []
    except Exception as e:
        logger.error(f"Error creating message: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
def create_conversation(db: Session, name: str) -> Conversation:
    logger.debug(f"Creating conversation with name: {name}")
    try:
        conversation = Conversation(name=name, dateCreated=datetime.utcnow())
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
        logger.info(f"Created conversation with ID: {conversation.id}")
        return conversation.id
    except Exception as e:
        logger.error(f"Error creating conversation: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def create_message(db: Session, conversation_id: str, content: str, role: str = "user") -> Message:
    logger.debug(f"Creating message for conversation {conversation_id}")
    try:
        message = Message(
            conversation_id=conversation_id,
            content=content,
            role=role,
            dateCreated=datetime.utcnow()
        )
        db.add(message)
        db.commit()
        db.refresh(message)
        logger.info(f"Created message with ID: {message.id}")
        return message
    except Exception as e:
        logger.error(f"Error creating message: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))