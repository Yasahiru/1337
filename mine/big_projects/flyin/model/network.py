from dataclasses import dataclass
from typing import Dict, List

from .connection import Connection
from .zone import Zone


@dataclass
class Network:
    nb_drones: int
    start_hub: Zone
    end_hub: Zone
    zones: Dict[str, Zone]
    connections: List[Connection]
    adjacency: dict[Zone, list[Connection]]
    current_turn: int = 0

    def capacity_Report(self) -> None:
        for conn in self.connections:
            print(conn.zone1, conn.zone2, sep="-")
