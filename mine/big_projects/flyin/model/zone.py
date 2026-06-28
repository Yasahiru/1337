from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from .zone_type import ZoneType, ZoneRole

if TYPE_CHECKING:
    from .drone import Drone


@dataclass
class Zone:
    x: int
    y: int
    name: str
    max_drones: int
    color: str = None
    zone_type: ZoneType = ZoneType.NORMAL
    zone_role: ZoneRole = ZoneRole.REGULAR
    current_drones: list["Drone"] = field(default_factory=list)
