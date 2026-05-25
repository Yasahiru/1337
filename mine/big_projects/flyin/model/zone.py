from dataclasses import dataclass, field
from typing import Union
from .zone_type import ZoneType, ZoneRole
from .color import Color
from .drone import Drone


@dataclass
class Zone:
    x: int
    y: int
    name: str
    max_drones: int
    color: Union[Color, None] = Color.Black
    zone_type: ZoneType = ZoneType.NORMAL
    zone_role: ZoneRole = ZoneRole.REGULAR
    current_drones: list[Drone] = field(default_factory=list)
