from fastapi import APIRouter
from app.api.api_v1.endpoints import transactions

api_router = APIRouter()
api_router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
