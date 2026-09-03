from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="Portfolio-ready production-style FastAPI REST API.",
)

app.include_router(router, prefix="/api/v1")

@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}
