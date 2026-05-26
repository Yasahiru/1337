from typing import List

from model.zone import Zone
from model.zone_type import ZoneRole, ZoneType


class Validator:
    def __init__(self, zones, connections) -> None:
        self.zones = zones
        self.conns = connections

    def zones_obj(self) -> List[Zone]:
        zones = []
        for zone in self.zones:
            meta = zone.get("meta_data", {})
            obj = Zone(
                name=zone["name"],
                x=zone["x"],
                y=zone["y"],
                color=meta.get("color"),
                max_drones=int(meta.get("max_drones", 1)),
                zone_type=(
                    ZoneType(meta["zone"])
                    if meta.get("zone") in ZoneType._value2member_map_
                    else ZoneType.NORMAL
                ),
                zone_role=(
                    ZoneRole(meta["zone_role"])
                    if meta.get("zone_role") in ZoneRole._value2member_map_
                    else ZoneRole.REGULAR
                ),
            )
            zones.append(obj)
        return zones
