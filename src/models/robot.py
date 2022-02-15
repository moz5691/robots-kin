from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class RobotSummary(models.Model):
    robot_id = fields.IntField()
    type = fields.TextField()
    time = fields.DatetimeField()
    kk_data_0 = fields.FloatField()
    kk_data_1 = fields.FloatField()
    kk_data_2 = fields.FloatField()
    kk_data_3 = fields.FloatField()
    kk_data_4 = fields.FloatField()
    kk_data_5 = fields.FloatField()
    kk_data_6 = fields.FloatField()
    kk_data_7 = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.robot_id


RobotSchema = pydantic_model_creator(RobotSummary)
