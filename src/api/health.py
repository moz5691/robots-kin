from fastapi import APIRouter, Depends
from src.config import get_settings, Settings

router = APIRouter()


@router.get("/ping/")
def health(settings: Settings = Depends(get_settings)):
    return {"health": "ok!", "environment": settings.environment, "testing": settings.testing}
