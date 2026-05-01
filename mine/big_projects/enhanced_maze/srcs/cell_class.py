from dataclasses import dataclass
from srcs.direction_class import Direction, ALL_DIRECTIONS


@dataclass
class Cell:

    x: int
    y: int
    visited: bool = False
    walls: int = ALL_DIRECTIONS

    def has_wall(self, direction: Direction) -> bool:
        """Check if a wall exists in the given direction."""
        return bool(self.walls & direction)

    def remove_wall(self, direction: Direction) -> None:
        """Remove a wall in the given direction."""
        self.walls &= ~direction

    def add_wall(self, direction: Direction) -> None:
        """Add a wall in the given direction."""
        self.walls |= direction

    def is_fully_bordered(self) -> bool:
        """Check if all walls are present."""
        return self.walls == ALL_DIRECTIONS
