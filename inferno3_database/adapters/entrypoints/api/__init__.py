from fastapi import APIRouter

from inferno3_database.adapters.entrypoints.api.v1 import (
    items_routes,
    health_routes,
    areas_routes,
)


api_router = APIRouter()
api_router.include_router(health_routes.router, prefix="", tags=["Health"])
api_router.include_router(items_routes.router, prefix="/v1/items", tags=["items_v1"])
api_router.include_router(areas_routes.router, prefix="/v1/areas", tags=["areas_v1"])
