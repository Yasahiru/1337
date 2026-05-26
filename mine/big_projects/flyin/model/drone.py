from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Union

from .drone_state import DroneState

if TYPE_CHECKING:
    from .connection import Connection
    from .zone import Zone


@dataclass
class Drone:
    drone_id: str
    state: DroneState
    curent_location: Union["Zone", "Connection"]
    remaining_turns: int
    is_delivered: bool = False
    planned_path: list["Zone"] = field(default_factory=list)
