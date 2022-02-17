from typing import Optional

from fastapi import APIRouter, Depends
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.requests import Request

from src.api.auth import get_user

router = APIRouter()


@router.get("/docs")
async def get_documentation(request: Request, user: Optional[dict] = Depends(get_user)):
    response = get_swagger_ui_html(openapi_url="/openapi.json", title="Documentation")
    return response
