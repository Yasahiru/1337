from dataclasses import dataclass
from typing import Union
from zone_type import ZoneType, ZoneRole
from color import Color


@dataclass
class Zone:
    x: int
    y: int
    name: str
    max_drones: int
    color: Union[Color, None] = Color.Black
    zone_type: ZoneType = ZoneType.NORMAL
    zone_role: ZoneRole = ZoneRole.REGULAR


t = {"k": {"colors": "red"}}
print(t["k"]["color"] | None)
