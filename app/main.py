from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="Production-ready task management API built with FastAPI for portfolio, internal tooling, and service integration use cases.",
)

app.include_router(router, prefix="/api/v1")

@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}
