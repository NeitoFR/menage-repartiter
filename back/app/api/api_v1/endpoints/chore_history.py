from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.chore_history import ChoreHistory
from app.schemas.chore_history import ChoreHistoryCreate, ChoreHistoryResponse

router = APIRouter()

@router.get("/", response_model=List[ChoreHistoryResponse])
def read_chore_history(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    history = db.query(ChoreHistory).offset(skip).limit(limit).all()
    return history

@router.post("/", response_model=ChoreHistoryResponse)
def create_chore_history(history: ChoreHistoryCreate, db: Session = Depends(get_db)):
    db_history = ChoreHistory(**history.dict())
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history

@router.get("/user/{user_id}", response_model=List[ChoreHistoryResponse])
def read_user_chore_history(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    history = db.query(ChoreHistory).filter(ChoreHistory.user_id == user_id).offset(skip).limit(limit).all()
    return history

@router.get("/task/{task_id}", response_model=List[ChoreHistoryResponse])
def read_task_chore_history(task_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    history = db.query(ChoreHistory).filter(ChoreHistory.task_id == task_id).offset(skip).limit(limit).all()
    return history 