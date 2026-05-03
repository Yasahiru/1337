from pydantic import BaseModel, Field, model_validator, StrictInt
from typing import Union
from zone_type import ZoneType, ZoneRole
from color import Color


class Zone(BaseModel):
    x: StrictInt = Field(ge=0)
    y: StrictInt = Field(ge=0)
    name: str = Field(min_length=2)
    color: Union[Color, None] = Color.Black
    max_drones: int = Field(default=1, ge=1)
    zone_type: ZoneType = ZoneType.NORMAL
    zone_role: ZoneRole = ZoneRole.REGULAR

    @model_validator(mode="before")
    def validate_logic_before(cls, data):
        if any(c in data.get("name") for c in (" ", "-")):
            raise ValueError(
                "Name should not contain spaces or dashes !!"
            )
        return data

    # @model_validator(mode="after")
    # def validate_logic_after(self) -> object:
    #     if self.current_drone_count() > self.max_drones:
    #         raise ValueError(
    #             f"Zone {self.name} exceed it's maximum capacity !!"
    #         )
    #     return self
