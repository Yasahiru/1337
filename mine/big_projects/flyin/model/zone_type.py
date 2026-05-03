from enum import Enum


class ZoneType(str, Enum):
    NORMAL = "NORMAL"
    BLOCKED = "BLOCKED"
    RESTRICTED = "RESTRICTED"
    PRIORITY = "PRIORITY"


class ZoneRole(str, Enum):
    START = "START"
    REGULAR = "REGULAR"
    END = "END"
