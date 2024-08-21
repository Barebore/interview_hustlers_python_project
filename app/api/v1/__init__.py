from fastapi import APIRouter

from . import demo, monitoring

router = APIRouter()
router.include_router(monitoring.router, tags=["monitoring"])
router.include_router(demo.router, tags=["demo"])
