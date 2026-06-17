from __future__ import annotations

from dataclasses import dataclass, field
from .drone_state import DroneState
from model.zone import Zone


@dataclass
class Drone:
    drone_id: str
    current_location: Zone
    state: DroneState = DroneState.WAITING
    is_delivered: bool = False
    assigned_path: list[str] = field(default_factory=list)
    path_index: int = 0
    start_turn: int = 0
