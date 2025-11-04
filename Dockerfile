FROM python:3.14.0-alpine3.22 as base

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD . /app
WORKDIR /app

RUN uv sync --locked
ENTRYPOINT uv run flask --app app run --host=0.0.0.0 --debug
