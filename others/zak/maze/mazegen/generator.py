import sys
from typing import List, Tuple, Optional
from collections import deque
from mazegen.grid import Grid
from mazegen.cell import Cell
import random


class MazeGenerator:
    """Generate a maze using the recursive backtracker (DFS) algorithm.

    Attributes:
        width (int): Number of columns in the maze.
        height (int): Number of rows in the maze.
        seed (Optional[int]): Random seed for reproducibility.
        perfect (bool): Whether the maze should be a perfect maze.
        entry_point (Tuple[int, int]): Entry coordinates (x, y).
        exit_point (Tuple[int, int]): Exit coordinates (x, y).
        grid (Grid): The generated maze grid.
    """

    def __init__(
        self,
        width: int,
        height: int,
        seed: Optional[int],
        perfect: bool,
        entry_point: Tuple[int, int],
        exit_point: Tuple[int, int]
    ) -> None:
        """Initialize and generate the maze.

        Args:
            width (int): Number of columns in the maze.
            height (int): Number of rows in the maze.
            seed (Optional[int]): Random seed for reproducibility.
            perfect (bool): Whether to generate a perfect maze.
            entry_point (Tuple[int, int]): Entry cell coordinates (x, y).
            exit_point (Tuple[int, int]): Exit cell coordinates (x, y).
        """
        self.width: int = width
        self.height: int = height
        self.seed: Optional[int] = seed
        self.perfect: bool = perfect
        self.entry_point: Tuple[int, int] = entry_point
        self.exit_point: Tuple[int, int] = exit_point

        if self.seed is not None:
            random.seed(self.seed)
        else:
            self.seed = int(random.randint(0, sys.maxsize))
            random.seed(self.seed)

        self.grid: Grid = Grid(self.width, self.height)

        self.stack: List[Cell] = [
            self.grid.get_cell(self.entry_point[0], self.entry_point[1])
        ]
        self.stack[0].visited = True

        self._generate()

    def _generate(self) -> None:
        """Generate the maze using the recursive backtracker algorithm.

        Carves passages by visiting unvisited neighbors randomly,
        backtracking when no unvisited neighbors remain.
        """
        while self.stack:
            unvisited_neighbors: List[Tuple[str, Cell]] = (
                self._get_unvisited_neighbors(self.stack[-1])
            )

            if unvisited_neighbors:
                direction, neighbor = random.choice(unvisited_neighbors)
                self.grid.open_wall(self.stack[-1], neighbor, direction)
                neighbor.visited = True
                self.stack.append(neighbor)
            else:
                self.stack.pop()

    def _get_unvisited_neighbors(self, cell: Cell) -> List[Tuple[str, Cell]]:
        """Return all unvisited neighbors of a given cell.

        Args:
            cell (Cell): The cell to check neighbors for.

        Returns:
            List[Tuple[str, Cell]]: List of (direction, neighbor) pairs
                where the neighbor has not yet been visited.
        """
        return [
            (direction, neighbor)
            for direction, neighbor in self.grid.get_neighbors(cell)
            if not neighbor.visited
        ]

    def solve(self) -> str:
        """Find the shortest path from entry to exit using BFS.

        Returns:
            str: A string of direction characters (N/E/S/W) representing
                the shortest path. Returns an empty string if no path exists.
        """
        entry: Cell = self.grid.get_cell(
            self.entry_point[0], self.entry_point[1]
        )
        exit_cell: Cell = self.grid.get_cell(
            self.exit_point[0], self.exit_point[1]
        )

        queue: deque[Tuple[Cell, List[str]]] = deque()
        queue.append((entry, []))
        visited: set[Cell] = {entry}

        while queue:
            current, path = queue.popleft()

            if current == exit_cell:
                return "".join(path)

            for direction, neighbor in self.grid.get_neighbors(current):
                if current.walls[direction] and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [direction]))

        return ""
