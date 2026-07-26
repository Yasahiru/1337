from typing import Any, Dict, List, Tuple
from zone_model import Zone
from connection import Connection
from zone_type import ZoneRole, ZoneType


class Validator:
    def __init__(
        self,
        zones: List[Dict[str, Any]],
        connections: List[Dict[str, Any]],
        nb_drones: int
    ) -> None:
        self.zones: List[Dict[str, Any]] = zones
        self.conns: List[Dict[str, Any]] = connections
        self.nb_drones = nb_drones

        self.graph: Dict[str, List[Tuple[str, int]]] = {}
        self.start: Zone | None = None
        self.end: Zone | None = None

    def zones_obj(self) -> List[Zone]:
        zones = []
        for z in self.zones:
            meta = z.get("meta_data", {})
            obj = Zone(
                name=z["name"],
                x=z["x"],
                y=z["y"],
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
            if z["kind"] == "start_hub":
                self.start = obj
                obj.zone_role = ZoneRole.START
                obj.max_drones = self.nb_drones
            elif z["kind"] == "end_hub":
                self.end = obj
                obj.zone_role = ZoneRole.END
                obj.max_drones = self.nb_drones

            zones.append(obj)
        return zones

    def connection_obj(self) -> List[Connection]:
        connections = []

        for conn in self.conns:
            meta = conn.get("meta_data", {})
            zone1 = conn["zone1"]
            zone2 = conn["zone2"]
            obj = Connection(
                zone1=zone1,
                zone2=zone2,
                name=f"{zone1}-{zone2}",
                current_drones=[],
                max_link_capacity=int(meta.get("max_link_capacity", 1))
            )
            connections.append(obj)
        return connections
