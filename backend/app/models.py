from sqlalchemy import Column, Integer, String, Numeric, Date, Boolean, ForeignKey, Enum, DateTime, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum


class OrganizationType(enum.Enum):
    business = "business"
    government = "government"


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(length=3), unique=True, nullable=False, index=True)
    name = Column(String(length=64), nullable=False)
    symbol = Column(String(length=8), nullable=False)
    decimals = Column(Integer, default=2)


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=256), nullable=False)
    currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)
    organization_type = Column(Enum(OrganizationType), default=OrganizationType.business, nullable=False)

    currency = relationship("Currency")
    users = relationship("User", back_populates="organization")
    accounts = relationship("Account", back_populates="organization")
    transactions = relationship("Transaction", back_populates="organization")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=256), unique=True, nullable=False, index=True)
    full_name = Column(String(length=256), nullable=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    role = Column(String(length=32), default="accountant")

    organization = relationship("Organization", back_populates="users")


class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    from_currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)
    to_currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)
    rate = Column(Numeric(18, 8), nullable=False)

    from_currency = relationship("Currency", foreign_keys=[from_currency_id])
    to_currency = relationship("Currency", foreign_keys=[to_currency_id])


class AccountType(enum.Enum):
    asset = "asset"
    liability = "liability"
    revenue = "revenue"
    expense = "expense"
    equity = "equity"


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    name = Column(String(length=256), nullable=False)
    code = Column(String(length=32), nullable=True)
    type = Column(Enum(AccountType), nullable=False)
    currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)

    organization = relationship("Organization", back_populates="accounts")
    currency = relationship("Currency")
    transactions = relationship("Transaction", back_populates="account")


class TaxCode(Base):
    __tablename__ = "tax_codes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=128), nullable=False)
    jurisdiction = Column(String(length=128), nullable=False)
    tax_type = Column(String(length=32), nullable=False)
    rate = Column(Numeric(10, 4), nullable=False)
    description = Column(Text, nullable=True)


class TransactionType(enum.Enum):
    income = "income"
    expense = "expense"
    transfer = "transfer"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String(length=512), nullable=True)
    amount = Column(Numeric(18, 2), nullable=False)
    currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    category = Column(String(length=128), nullable=True)
    subcategory = Column(String(length=128), nullable=True)
    tax_code_id = Column(Integer, ForeignKey("tax_codes.id"), nullable=True)
    tax_amount = Column(Numeric(18, 2), nullable=True)
    exchange_rate_id = Column(Integer, ForeignKey("exchange_rates.id"), nullable=True)
    is_recurring = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), nullable=False)

    organization = relationship("Organization", back_populates="transactions")
    account = relationship("Account", back_populates="transactions")
    currency = relationship("Currency")
    tax_code = relationship("TaxCode")
    exchange_rate = relationship("ExchangeRate")
