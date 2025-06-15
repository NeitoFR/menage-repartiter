from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class HouseholdChore(BaseModel):
    __tablename__ = "household_chores"

    nom = Column(String(30), nullable=False)
    periodicity = Column(Integer, nullable=False)
    
    # Relationships
    chore_history = relationship("ChoreHistory", back_populates="task") 