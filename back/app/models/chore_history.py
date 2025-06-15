from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class ChoreHistory(BaseModel):
    __tablename__ = "chores_history"

    done_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    task_id = Column(Integer, ForeignKey("household_chores.id"), nullable=False)

    # Relationships
    user = relationship("User", back_populates="chore_history")
    task = relationship("HouseholdChore", back_populates="chore_history") 