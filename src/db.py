import logging
import os
import logging

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise, run_async

log = logging.getLogger("uvicorn")

TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["src.models.robot"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["src.models.robot"]},
        generate_schemas=True,  # set False if you use migration
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    # provision for manual table creation
    # set generate_schemas=False to prevent auto generation of table
    # if you need to use migration.

    log.info("Initializing ORM...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["models.robot"]},
    )
    log.info("Generating database schema via ORM...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
