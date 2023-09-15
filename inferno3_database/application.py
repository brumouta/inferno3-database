from fastapi import FastAPI

from inferno3_database.adapters.db.database import start_db
from inferno3_database.adapters.entrypoints.api import api_router


def create_app() -> FastAPI:
    fastapi = FastAPI()
    fastapi.include_router(api_router)
    return fastapi


app = create_app()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client, app.db = start_db()


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()
