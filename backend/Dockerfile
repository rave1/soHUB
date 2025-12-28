FROM python:3.14.0-alpine3.22 as base

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_PROJECT_ENVIRONMENT=/usr/local
WORKDIR /code
COPY ../pyproject.toml .
COPY ../uv.lock .
COPY . .

RUN uv sync --locked

WORKDIR /code/app

CMD ["fastapi", "run", "main.py", "--port", "8000"]
