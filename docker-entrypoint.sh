#!/bin/sh

set -e

. /app/.venv/bin/activate

exec uvicorn "inferno3_database.application:app" --host 0.0.0.0 --port 8000
