from __future__ import annotations

from dataclasses import dataclass
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from connection import Connection
    from zone_model import Zone


@dataclass
class Drone:
    drone_id: str
    assigned_path: List[Zone]

    current_location: Zone
    current_connection: Connection | None = None

    target_zone: Zone | None = None
    turns_left: int = 0
    is_delivered: bool = False
    path_index: int = 0
