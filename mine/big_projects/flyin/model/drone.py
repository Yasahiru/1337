from dataclasses import dataclass
from .connection import Connection
from typing import Union
from zone import Zone


@dataclass
class Drone:
    drone_id: str
    state: str
    curent_location: Union[Zone, Connection]
    remaining_turns: int
    is_delivered: bool = False
