# TrackYourFunds

A business-first finance tracking application scaffold with multi-currency support, tax calculation readiness, and accountant-focused workflows.

## Project structure

- `backend/` — FastAPI backend with PostgreSQL support, core accounting models, transaction APIs, tax codes, and currency management.
- `frontend/` — React + TypeScript web client shell for dashboards and business reporting.

## Key capabilities included

- Multi-tenant business model with `Organization`, `Account`, `Transaction`, `TaxCode`, and `ExchangeRate` entities
- Multi-currency support (USD and Eastern Caribbean currency ready)
- Tax code structure for VAT/GST/sales tax support
- Basic transaction API and currency creation endpoint
- Frontend dashboard placeholder for business metrics

## Quick start

### Backend

1. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
2. Install dependencies:
   ```bash
   cd backend
   poetry install
   ```
3. Start the API server:
   ```bash
   poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```

## Notes

- The backend uses `.env` for `DATABASE_URL` configuration.
- The current scaffold is designed for business and future government use, with manual input workflows and later support for VAT returns and accounting automation.
