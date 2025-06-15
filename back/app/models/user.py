from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    nom = Column(String(30), nullable=False)
    
    # Relationships
    chore_history = relationship("ChoreHistory", back_populates="user") 