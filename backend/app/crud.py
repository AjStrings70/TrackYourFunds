from sqlalchemy.orm import Session
from decimal import Decimal
from datetime import datetime
from typing import Optional

import app.models as models
import app.schemas as schemas


def get_currency_by_code(db: Session, code: str) -> Optional[models.Currency]:
    return db.query(models.Currency).filter(models.Currency.code == code).first()


def create_currency(db: Session, currency: schemas.CurrencyCreate) -> models.Currency:
    db_obj = models.Currency(**currency.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_organization(db: Session, organization: schemas.OrganizationCreate) -> models.Organization:
    db_obj = models.Organization(**organization.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_account(db: Session, account: schemas.AccountCreate) -> models.Account:
    db_obj = models.Account(**account.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_tax_code(db: Session, tax_code: schemas.TaxCodeCreate) -> models.TaxCode:
    db_obj = models.TaxCode(**tax_code.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_transaction(db: Session, transaction: schemas.TransactionCreate) -> models.Transaction:
    payload = transaction.model_dump()
    payload["created_at"] = datetime.utcnow()
    if payload.get("amount") is not None:
        payload["amount"] = Decimal(str(payload["amount"]))
    if payload.get("tax_amount") is not None:
        payload["tax_amount"] = Decimal(str(payload["tax_amount"]))
    db_obj = models.Transaction(**payload)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transaction).offset(skip).limit(limit).all()


def get_exchange_rate(db: Session, from_code: str, to_code: str, date_value):
    return (
        db.query(models.ExchangeRate)
        .join(models.Currency, models.ExchangeRate.from_currency)
        .join(models.Currency, models.ExchangeRate.to_currency)
        .filter(models.ExchangeRate.from_currency.has(code=from_code))
        .filter(models.ExchangeRate.to_currency.has(code=to_code))
        .filter(models.ExchangeRate.date == date_value)
        .first()
    )
