from dataclasses import dataclass
from typing import List, Tuple
import random


@dataclass
class Cell:
    north: bool = True
    east: bool = True
    south: bool = True
    west: bool = True


@dataclass
class Maze:
    width: int
    height: int
    grid: List[List[Cell]]
    entry: Tuple[int, int]
    exit: Tuple[int, int]
    # path: Tuple[Tuple[int, int]]
    def getCell(self, x : int, y : int) -> Cell:
        return self.grid[y][x]


def generate_fake_maze(width: int, height: int) -> Maze:
    """Generate a simple fake maze for testing display."""

    # create grid with all walls closed
    grid = [[Cell() for _ in range(width)] for _ in range(height)]

    # randomly open walls between neighbors
    for y in range(height):
        for x in range(width):

            # open east wall
            if x < width - 1 and random.choice([True, False]):
                grid[y][x].east = False
                grid[y][x + 1].west = False

            # open south wall
            if y < height - 1 and random.choice([True, False]):
                grid[y][x].south = False
                grid[y + 1][x].north = False

    entry = (0, 0)
    exit = (width - 1, height - 1)

    return Maze(width, height, grid, entry, exit)
