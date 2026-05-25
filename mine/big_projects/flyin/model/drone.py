from dataclasses import dataclass
from typing import Union, TYPE_CHECKING
from drone_state import DroneState

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
