from pydantic import BaseModel, Field, model_validator, StrictInt
# from __future__ import annotations
from typing import List
from drone import Drone


class Connection(BaseModel):
    zone1: str = Field(min_length=1)
    zone2: str = Field(min_length=1)
    max_link_capacity: StrictInt = Field(ge=1)
    current_drones: List["Drone"] = Field(default_factory=list)

    def current_drone_count(self) -> int:
        return len(self.current_drones)

    @model_validator(mode="after")
    def validate_logic_after(self) -> None:
        if self.current_drone_count() > self.max_link_capacity:
            raise ValueError(
                f"Connection {self.zone1}-{self.zone2} "
                "exceed it's maximum capacity !!"
            )
