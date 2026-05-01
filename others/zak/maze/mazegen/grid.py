from typing import List, Tuple, Dict
from mazegen.cell import Cell


OPPOSITE: Dict[str, str] = {
    "N": "S",
    "E": "W",
    "S": "N",
    "W": "E"
}


class Grid:
    """Represent a 2D grid of cells forming a maze.

    Attributes:
        width (int): Number of columns in the grid.
        height (int): Number of rows in the grid.
        cells (List[List[Cell]]): 2D list of Cell objects indexed by [y][x].
    """

    def __init__(self, width: int, height: int) -> None:
        """Initialize the grid with all cells having walls closed.

        Args:
            width (int): Number of columns in the grid.
            height (int): Number of rows in the grid.
        """
        self.width: int = width
        self.height: int = height
        self.cells: List[List[Cell]] = [
            [Cell(x, y) for x in range(width)]
            for y in range(height)
        ]

    def get_cell(self, x: int, y: int) -> Cell:
        """Return the cell at position (x, y).

        Args:
            x (int): Horizontal position.
            y (int): Vertical position.

        Returns:
            Cell: The cell at the given coordinates.
        """
        return self.cells[y][x]

    def in_bounds(self, x: int, y: int) -> bool:
        """Check if coordinates are within the grid boundaries.

        Args:
            x (int): Horizontal position to check.
            y (int): Vertical position to check.

        Returns:
            bool: True if (x, y) is within bounds, False otherwise.
        """
        x_in_bounds: bool = 0 <= x < self.width
        y_in_bounds: bool = 0 <= y < self.height
        return x_in_bounds and y_in_bounds

    def get_neighbors(self, cell: Cell) -> List[Tuple[str, Cell]]:
        """Return all valid in-bounds neighbors of a cell.

        Args:
            cell (Cell): The cell to find neighbors for.

        Returns:
            List[Tuple[str, Cell]]: List of (direction, neighbor) pairs
                for all valid neighboring cells.
        """
        directions: Dict[str, Tuple[int, int]] = {
            "N": (cell.x, cell.y - 1),
            "E": (cell.x + 1, cell.y),
            "S": (cell.x, cell.y + 1),
            "W": (cell.x - 1, cell.y)
        }
        neighbors: List[Tuple[str, Cell]] = []

        for key, (x, y) in directions.items():
            if self.in_bounds(x, y):
                neighbors.append((key, self.cells[y][x]))

        return neighbors

    def open_wall(self, cell: Cell, neighbor: Cell, direction: str) -> None:
        """Open the wall between two adjacent cells in both directions.

        Args:
            cell (Cell): The origin cell.
            neighbor (Cell): The neighboring cell to open the wall towards.
            direction (str): Direction from cell to neighbor ('N','E','S','W').
        """
        cell.walls[direction] = True
        neighbor.walls[OPPOSITE[direction]] = True
