from enum import IntEnum


class Direction(IntEnum):
    N = 1
    E = 2
    S = 4
    W = 8

    def delta(self) -> tuple[int, int]:
        if self == Direction.N:
            return (0, -1)
        elif self == Direction.S:
            return (0, 1)
        elif self == Direction.E:
            return (1, 0)
        elif self == Direction.W:
            return (-1, 0)
        raise ValueError("Invalid Direction")

    def opposite(self) -> "Direction":
        if self == Direction.N:
            return Direction.S
        elif self == Direction.S:
            return Direction.N
        elif self == Direction.E:
            return Direction.W
        elif self == Direction.W:
            return Direction.E


ALL_DIRECTIONS = Direction.N | Direction.E | Direction.S | Direction.W
