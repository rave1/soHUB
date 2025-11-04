FROM python:3.14.0-alpine3.22 as base

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
ADD ../pyproject.toml .
ADD ../uv.lock .
ADD *.py .

RUN uv sync --locked
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
