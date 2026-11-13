# Task Management API

A professional, production-oriented REST API for managing tasks, built with **FastAPI, SQLModel, Pydantic, SQLite, Docker, and Pytest**. The application is structured to support portfolio presentation, internal tooling, and extension into larger service-driven workflows.

## Features

- RESTful CRUD operations for task management
- Pydantic-based request and response validation
- SQLModel integration for database modeling
- FastAPI dependency injection for clean service composition
- Consistent HTTP error handling
- Health-check endpoint for monitoring
- Automated API testing
- Dockerized deployment support
- Interactive Swagger/OpenAPI documentation

## Project structure

```text
app/
  api/routes.py
  core/config.py
  db/session.py
  models/task.py
  main.py
tests/
  test_api.py
Dockerfile
docker-compose.yml
requirements.txt
```

## Local development

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
python -m app.db.init_db
uvicorn app.main:app --reload
```

Access the service at:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health check: http://127.0.0.1:8000/health

## Testing

```bash
pytest
```

## Docker

```bash
docker compose up --build
```

## Example request

Create a task:

```http
POST /api/v1/tasks
Content-Type: application/json

{
  "title": "Implement reporting workflow",
  "description": "Define the workflow for operational reporting and review",
  "completed": false
}
```

This project is intentionally structured as a clean foundation for a production-ready service. For a full deployment, consider PostgreSQL, Alembic migrations, JWT or OAuth2 authentication, rate limiting, structured logging, CI/CD workflows, and environment-specific secret management.
