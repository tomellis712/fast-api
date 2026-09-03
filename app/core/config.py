from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Portfolio Task API"
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "change-me-in-production"

settings = Settings()
