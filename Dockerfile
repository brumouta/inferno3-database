FROM --platform=linux/amd64 python:3.12-alpine AS base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base AS builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.6.1

RUN apk add --no-cache \
        curl \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile=minimal && \
    source "$HOME"/.cargo/env && \
    pip install --no-cache-dir poetry=="$POETRY_VERSION"

COPY pyproject.toml poetry.lock README.md ./

COPY inferno3_database ./inferno3_database

RUN poetry config virtualenvs.in-project true
RUN poetry install --only=main --no-root --no-interaction
RUN poetry build

FROM base AS final

RUN addgroup -S i3db \
    && adduser -S i3db -G i3db

COPY --from=builder /app/.venv ./.venv
COPY --from=builder /app/dist .
COPY docker-entrypoint.sh .
COPY inferno3_database/config.yaml .

ARG DATABASE_URL
ENV DATABASE_URL $DATABASE_URL
ARG DATABASE_NAME
ENV DATABASE_NAME $DATABASE_NAME

RUN ./.venv/bin/pip install ./*.whl

USER i3db
CMD ["./docker-entrypoint.sh"]
