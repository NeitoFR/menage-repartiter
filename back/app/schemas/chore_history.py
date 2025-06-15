from pydantic import BaseModel
from datetime import date
from typing import Optional

class ChoreHistoryBase(BaseModel):
    done_date: date
    user_id: int
    task_id: int

class ChoreHistoryCreate(ChoreHistoryBase):
    pass

class ChoreHistoryResponse(ChoreHistoryBase):
    id: int

    class Config:
        from_attributes = True 