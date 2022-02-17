from typing import List

from pydantic import BaseModel


class Header(BaseModel):
    timestamp_sec: int = 1559752729
    robot_id: int = 123
    sys_type: str = "AAA"


class Data(BaseModel):
    kk_data: list[float] = [0, 0, 0, 0, 0, 0, 0, 0]
    kk_header: Header


class Robot(BaseModel):
    kk_dict: Data


class RobotPayloadSchema(BaseModel):
    robot_id: int
    type: str
    time: int  # todo: convert it to UTC
    kk_data_0: float
    kk_data_1: float
    kk_data_2: float
    kk_data_3: float
    kk_data_4: float
    kk_data_5: float
    kk_data_6: float
    kk_data_7: float


class RobotAvgResponseSchema(BaseModel):
    robot_id: int
    avg_kk_data: List[float]
    robots_count: int
    robots: List[dict] | None

    # created_at: datetime


class RobotResponseSchema(BaseModel):
    id: int
    robot_id: int


class ErrorResponseSchema(BaseModel):
    detail: str
