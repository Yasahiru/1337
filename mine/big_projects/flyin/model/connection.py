from dataclasses import dataclass, field
from typing import List
from .zone import Zone
from .drone import Drone


@dataclass
class Connection:
    zone1: Zone
    zone2: Zone
    max_link_capacity: int
    current_drones: List[Drone] = field(default_factory=list)

    def current_drone_count(self) -> int:
        return len(self.current_drones)
