import logging
from fastapi import FastAPI
from src.api import health, robots, auth
from src.db import init_db
from starlette.middleware.sessions import SessionMiddleware


log = logging.getLogger("uvicorn")

description = """
Robots Kinematics API helps you do awesome stuff. 🚀
"""


def create_application() -> FastAPI:
    application = FastAPI(
        title="Robots Kinematics",
        version="0.0.1",
        contact={
            "name": "Chan Ho Ahn",
            "email": "moz5691@gmail.com",
        },
        docs_url=None,
        redoc_url=None,
    )
    application.add_middleware(SessionMiddleware, secret_key="!secret!")
    application.include_router(health.router, prefix="/health", tags=["Health"])
    application.include_router(auth.router, prefix="", tags=["Auth"])
    application.include_router(robots.router, prefix="/robots", tags=["Robots"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
