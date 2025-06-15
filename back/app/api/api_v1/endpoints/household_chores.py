from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.household_chore import HouseholdChore
from app.schemas.household_chore import HouseholdChoreCreate, HouseholdChoreResponse

router = APIRouter()

@router.get("/", response_model=List[HouseholdChoreResponse])
def read_household_chores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    chores = db.query(HouseholdChore).offset(skip).limit(limit).all()
    return chores

@router.post("/", response_model=HouseholdChoreResponse)
def create_household_chore(chore: HouseholdChoreCreate, db: Session = Depends(get_db)):
    db_chore = HouseholdChore(**chore.dict())
    db.add(db_chore)
    db.commit()
    db.refresh(db_chore)
    return db_chore

@router.get("/{chore_id}", response_model=HouseholdChoreResponse)
def read_household_chore(chore_id: int, db: Session = Depends(get_db)):
    chore = db.query(HouseholdChore).filter(HouseholdChore.id == chore_id).first()
    if chore is None:
        raise HTTPException(status_code=404, detail="Chore not found")
    return chore 