from pydantic import BaseModel
from typing import Optional, List

class HouseholdChoreBase(BaseModel):
    nom: str
    periodicity: int

class HouseholdChoreCreate(HouseholdChoreBase):
    pass

class HouseholdChoreResponse(HouseholdChoreBase):
    id: int

    class Config:
        from_attributes = True 