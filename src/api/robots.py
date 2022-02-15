from typing import List
from fastapi import APIRouter, HTTPException
from src.schemas.robot import RobotResponseSchema, RobotPayloadSchema, Robot, RobotAvgResponseSchema, ErrorResponseSchema
from src.models.robot import RobotSchema
from src.crud import robots

router = APIRouter()


@router.post("/", response_model=RobotResponseSchema)
async def add_robot(json_payload: Robot):
    payload = {
        "robot_id": json_payload.kk_dict.kk_header.robot_id,
        "type": json_payload.kk_dict.kk_header.sys_type,
        "time": json_payload.kk_dict.kk_header.timestamp_sec,
        "kk_data_0": json_payload.kk_dict.kk_data[0],
        "kk_data_1": json_payload.kk_dict.kk_data[1],
        "kk_data_2": json_payload.kk_dict.kk_data[2],
        "kk_data_3": json_payload.kk_dict.kk_data[3],
        "kk_data_4": json_payload.kk_dict.kk_data[4],
        "kk_data_5": json_payload.kk_dict.kk_data[5],
        "kk_data_6": json_payload.kk_dict.kk_data[6],
        "kk_data_7": json_payload.kk_dict.kk_data[7]
    }

    res = await robots.post(payload)

    response_obj = {
        "id": res["id"],
        "robot_id": res["robot_id"],
    }

    return response_obj


@router.get("/", response_model=List[RobotSchema])
async def get_all_robots() -> List[RobotSchema]:
    return await robots.get_all()


@router.get("/{id}/", response_model=RobotSchema)
async def get_by_id(id: int) -> RobotSchema:
    result = await robots.get_by_id(id)

    if not result:
        raise HTTPException(status_code=404, detail=f"id: {id} is not found")

    return result


@router.get("/robot_id/{robot_id}/", response_model=RobotAvgResponseSchema)
async def get_by_robot_id(robot_id: int) -> RobotAvgResponseSchema:
    avg_kk_data = [.0] * 8
    result = await robots.get_by_robot_id(robot_id)

    if not result:
        raise HTTPException(status_code=404, detail=f"Robot id: {robot_id} is not found")

    robots_count = len(result)

    for i in range(len(avg_kk_data)):
        for r in result:
            avg_kk_data[i] += r[f"kk_data_{i}"]
        avg_kk_data[i] /= len(result)

    response_obj = {
        "robot_id": robot_id,
        "avg_kk_data": avg_kk_data,
        "robots_count": robots_count,
        "robots": result,
    }
    return response_obj


@router.delete("/{id}/", response_model=RobotResponseSchema)
async def delete_by_id(id: int) -> dict:
    result: dict | None = await robots.get_by_id(id)
    if not result:
        raise HTTPException(status_code=404, detail="Robot not found")
    await robots.delete_by_id(id)

    return result


@router.delete("/robot_id/{robot_id}/", response_model=List[RobotSchema])
async def delete_by_robot_id(robot_id: int):
    result = await robots.get_by_robot_id(robot_id)
    if not result:
        raise HTTPException(status_code=404, detail=f"Robot id: {robot_id} is not found")
    await robots.delete_by_robot_id(robot_id)

    return result
