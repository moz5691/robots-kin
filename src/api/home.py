from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from src.api.auth import get_user

router = APIRouter()

BASE_PATH = Path(__file__).parent.parent.resolve()
print("BASE_PATH ", BASE_PATH)
templates = Jinja2Templates(directory=f"{BASE_PATH}/templates")


@router.get("/")
async def home(request: Request):
    user = request.session.get("user")
    if user is not None:
        email = user["email"]
        return templates.TemplateResponse(
            "home.html", context={"request": request, "email": email}
        )
    return templates.TemplateResponse(
        "login.html", context={"request": request, "user": user}
    )


@router.get("/finder")
def form_post(request: Request, user: Optional[dict] = Depends(get_user)):
    user = request.session.get("user")
    return templates.TemplateResponse(
        "form.html", context={"request": request, "user": user}
    )
