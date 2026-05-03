from pydantic import BaseModel, Field, model_validator, StrictInt
from typing import Union
from zone import Zone
from connection import Connection


class Drone(BaseModel):
    drone_id: str = Field(min_length=2)
    curent_location: Union["Zone", "Connection"] = None
    state: str = None
    remaining_turns: StrictInt = 0
    is_delivered: bool = False

    @model_validator(mode="after")
    def validate_logic(self) -> object:
        if not self.drone_id.startswith("D"):
            raise ValueError("drone ID must start with 'D'")
        return self
