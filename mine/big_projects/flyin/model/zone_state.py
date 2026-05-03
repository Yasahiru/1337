from pydantic import Field
from drone import Drone
from zone import Zone
from zone_type import ZoneRole


class ZoneState:
    def __init__(self, zone: Zone):
        self.zone = zone
        self.current_drones: list["Drone"] = Field(default_factory=list)

    def exceed_drone_capacity(self) -> bool:
        if self.zone.zone_role in [ZoneRole.START, ZoneRole.END]:
            return False
        return len(self.current_drones) > self.zone.max_drones
