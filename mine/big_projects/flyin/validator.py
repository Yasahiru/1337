from model.connection import Connection
from model.network import Network
from model.zone import Zone
from typing import List


class Validator:
    def __init__(self, zones, connections) -> None:
        self.zones = zones
        self.conns = connections

    def zones_obj(self) -> List[Zone]:
        zones = []
        for zone in self.zones:
            obj = Zone(
                name=zone["name"],
                x=zone["x"],
                y=zone["y"],
                color=zone["meta_data"]["color"]
            )
            zones.append(obj)
        return zones
