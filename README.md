# Portfolio FastAPI Task API

A clean, portfolio-ready REST API built with **FastAPI, SQLModel, Pydantic, SQLite, Docker, and Pytest**.

## Features

- RESTful CRUD API
- Pydantic request/response validation
- SQLModel database layer
- Dependency injection with FastAPI
- HTTP error handling
- Health-check endpoint
- Automated API test
- Docker support
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

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
python -m app.db.init_db
uvicorn app.main:app --reload
```

Open:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health: http://127.0.0.1:8000/health

## Run tests

```bash
pytest
```

## Docker

```bash
docker compose up --build
```

## Example API

Create a task:

```http
POST /api/v1/tasks
Content-Type: application/json

{
  "title": "Build FastAPI portfolio",
  "description": "Create a production-style API",
  "completed": false
}
```

This project is intentionally structured as a portfolio starter. For a production deployment, add PostgreSQL, Alembic migrations, JWT/OAuth2 authentication, rate limiting, structured logging, CI/CD, and environment-specific secrets.
