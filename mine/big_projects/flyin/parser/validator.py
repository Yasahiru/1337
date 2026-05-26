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
                color=zone["meta_data"]["color"],
                max_drones=(
                    int(zone["meta_data"]["max_drones"])
                    if "max_drones" in zone["meta_data"] else 1
                ),
                zone_type=(
                    zone["meta_data"]["zone"]
                    if "zone" in zone["meta_data"] else None
                ),
                zone_role=(
                    zone["meta_data"]["zone_role"]
                    if "zone_role" in zone["meta_data"] else None
                )
            )
            zones.append(obj)
        return zones
