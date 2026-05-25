from enum import Enum


class ZoneType(str, Enum):
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


class ZoneRole(str, Enum):
    START = "start"
    REGULAR = "regular"
    END = "end"
