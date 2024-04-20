import uuid
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
)

from .database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Conversation(Base):
    __tablename__ = "conversation"
    
    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True,default=uuid.uuid4
    )
    dateCreated = Column(DateTime)
    name = Column(String)
    messages = relationship("Message", back_populates="conversation")
    
class Message(Base):

    __tablename__ = "messages"
    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    
    conversation_id = Column(
        UUID(as_uuid=True), ForeignKey("conversation.id"), index=True
    )
    content = Column(String)
    role = Column(String, default="user")
    dateCreated = Column(DateTime)
    conversation = relationship("Conversation", back_populates="messages")