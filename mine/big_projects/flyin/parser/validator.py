from typing import List
from model.zone import Zone
from model.connection import Connection
from model.zone_type import ZoneRole, ZoneType


class Validator:
    def __init__(self, zones, connections) -> None:
        self.zones = zones
        self.conns = connections
        self.graph = {}
        self.start = None
        self.end = None

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
            if zone["kind"] == "start_hub":
                self.start = obj
                obj.zone_role = ZoneRole.START
            elif zone["kind"] == "end_hub":
                self.end = obj
                obj.zone_role = ZoneRole.END

            zones.append(obj)
        return zones

    def connection_obj(self) -> List[Zone]:
        connections = []

        for conn in self.conns:
            meta = conn.get("meta_data", {})
            zone1 = conn.get("zone1")
            zone2 = conn.get("zone2")
            obj = Connection(
                zone1=zone1,
                zone2=zone2,
                name=f"{zone1}-{zone2}",
                current_drones=[],
                max_link_capacity=int(meta.get("max_link_capacity", 1))
            )
            connections.append(obj)
        return connections
