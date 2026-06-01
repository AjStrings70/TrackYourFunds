from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=schemas.TransactionRead)
def create_transaction(payload: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, payload)


@router.get("/", response_model=List[schemas.TransactionRead])
def list_transactions(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=500), db: Session = Depends(get_db)):
    return crud.get_transactions(db, skip=skip, limit=limit)


@router.post("/currencies", response_model=schemas.CurrencyRead)
def create_currency(payload: schemas.CurrencyCreate, db: Session = Depends(get_db)):
    existing = crud.get_currency_by_code(db, payload.code)
    if existing:
        raise HTTPException(status_code=400, detail="Currency already exists")
    return crud.create_currency(db, payload)
