from datetime import date, datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class CurrencyBase(BaseModel):
    code: str
    name: str
    symbol: str
    decimals: int = 2


class CurrencyCreate(CurrencyBase):
    pass


class CurrencyRead(CurrencyBase):
    id: int

    model_config = {
        "from_attributes": True,
    }


class OrganizationCreate(BaseModel):
    name: str
    currency_id: int
    organization_type: str = "business"


class OrganizationRead(BaseModel):
    id: int
    name: str
    currency_id: int
    organization_type: str

    model_config = {
        "from_attributes": True,
    }


class AccountType(str, Enum):
    asset = "asset"
    liability = "liability"
    revenue = "revenue"
    expense = "expense"
    equity = "equity"


class AccountCreate(BaseModel):
    organization_id: int
    name: str
    type: AccountType
    currency_id: int
    code: Optional[str] = None


class AccountRead(AccountCreate):
    id: int

    model_config = {
        "from_attributes": True,
    }


class TaxCodeBase(BaseModel):
    name: str
    jurisdiction: str
    tax_type: str
    rate: float
    description: Optional[str] = None


class TaxCodeCreate(TaxCodeBase):
    pass


class TaxCodeRead(TaxCodeBase):
    id: int

    model_config = {
        "from_attributes": True,
    }


class TransactionType(str, Enum):
    income = "income"
    expense = "expense"
    transfer = "transfer"


class TransactionBase(BaseModel):
    organization_id: int
    account_id: int
    date: date
    description: Optional[str] = None
    amount: float
    currency_id: int
    transaction_type: TransactionType
    category: Optional[str] = None
    subcategory: Optional[str] = None
    tax_code_id: Optional[int] = None
    tax_amount: Optional[float] = None
    exchange_rate_id: Optional[int] = None
    is_recurring: bool = False


class TransactionCreate(TransactionBase):
    pass


class TransactionRead(TransactionBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }
