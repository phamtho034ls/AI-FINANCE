from fastapi import FastAPI
from src.api.routes import health, predictions

app = FastAPI(title="AI-Finance API", version="1.0.0")
app.include_router(health.router)
app.include_router(predictions.router, prefix="/api/v1")
