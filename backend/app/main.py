from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.api_v1.api import api_router
from .db.session import engine
from .db.base import Base

# Create database tables on startup for development/demo purposes.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TrackYourFunds Business Finance API",
    description="Business-focused spending, saving, income, tax, and currency analytics",
    version="0.1.0",
)

origins = [
    "http://localhost:5173",
    # Add your deployed frontend origin(s) here, e.g. "https://your-app.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")
