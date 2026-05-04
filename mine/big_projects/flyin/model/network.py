from pydantic import BaseModel, Field, model_validator, StrictInt
from typing import Dict, List
from zone import Zone
from connection import Connection
# from __future__ import annotations


class Network(BaseModel):
    nb_drones: StrictInt = Field(ge=1)
    start_hub: Zone = None
    end_hub: Zone = None
    zones: Dict = {}
    connections: List[Connection] = Field(default_factory=list)
    current_turn: StrictInt = 0
    capacity_info_enabled: bool = False

    @model_validator(mode="after")
    def validate_logic(self) -> None:
        ...

    def capacity_Report(self) -> None:
        for conn in self.connections:
            print(conn.zone1, conn.zone2, sep="-")
