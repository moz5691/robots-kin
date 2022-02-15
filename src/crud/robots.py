import datetime
from typing import List, Union, Any
from src.models.robot import RobotSummary
from src.schemas.robot import RobotPayloadSchema
from datetime import datetime


async def post(payload: RobotPayloadSchema) -> dict[str, Any]:
    print("post payload --->", payload)
    robot = RobotSummary(
        robot_id=payload["robot_id"],
        type=payload["type"],
        time=datetime.utcfromtimestamp(payload["time"]),
        kk_data_0=payload["kk_data_0"],
        kk_data_1=payload["kk_data_1"],
        kk_data_2=payload["kk_data_2"],
        kk_data_3=payload["kk_data_3"],
        kk_data_4=payload["kk_data_4"],
        kk_data_5=payload["kk_data_5"],
        kk_data_6=payload["kk_data_6"],
        kk_data_7=payload["kk_data_7"],
    )

    await robot.save()

    return {"id": robot.id, "robot_id": robot.robot_id}


async def get_all() -> List:
    robots = await RobotSummary.all().values()
    return robots


async def get_by_id(id: int) -> Union[dict, None]:
    robot = await RobotSummary.filter(id=id).first().values()
    if not robot:
        return None
    return robot


async def get_by_robot_id(robot_id: int) -> Union[List[dict],None]:
    robots = await RobotSummary.filter(robot_id=robot_id).values()
    if len(robots) == 0:
        return None

    return robots


async def delete_by_id(id: int) -> int:
    robot = await RobotSummary.filter(id=id).first().delete()
    return robot


async def delete_by_robot_id(robot_id: int):
    robots = await RobotSummary.filter(robot_id=robot_id).delete()
    return robots

