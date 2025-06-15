from fastapi import APIRouter
from app.api.api_v1.endpoints import users, household_chores, chore_history

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(household_chores.router, prefix="/chores", tags=["household chores"])
api_router.include_router(chore_history.router, prefix="/history", tags=["chore history"]) 