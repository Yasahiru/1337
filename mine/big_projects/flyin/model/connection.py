from dataclasses import dataclass
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .zone import Zone
    from .drone import Drone


@dataclass
class Connection:
    zone1: "Zone"
    zone2: "Zone"
    name: str
    max_link_capacity: int
    current_drones: List["Drone"]

    def current_drone_count(self) -> int:
        return len(self.current_drones)
