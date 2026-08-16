from typing import List, Tuple, Optional, Set
from .cell_class import Cell
from .direction_class import Direction, ALL_DIRECTIONS
import time


class Maze:
    """Represents the maze grid."""

    def __init__(
        self,
        width: int,
        height: int,
        entry: Tuple[int, int],
        _exit: Tuple[int, int],
    ) -> None:

        self.width = width
        self.height = height
        self.entry = entry
        self.exit = _exit
        self.grid: List[List[Cell]] = []
        self.cells_42: Set[Tuple[int, int]] = set()
        self.initialize_grid()

    def initialize_grid(self) -> None:
        """initializing the grid"""
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Cell(x, y))
            self.grid.append(row)

    def reset_maze(self) -> None:
        """Full reset: reset visited status AND restore all walls."""
        self.cells_42 = set()
        for row in self.grid:
            for cell in row:
                cell.visited = False
                cell.walls = ALL_DIRECTIONS

    def get_cell(self, x: int, y: int) -> Cell:
        """Return the cell at the given coordinates."""
        return self.grid[y][x]

    def in_bounds(self, x: int, y: int) -> bool:
        """Check if coordinates are inside the maze."""
        return 0 <= x < self.width and 0 <= y < self.height

    def reset_visits(self) -> None:
        for row in self.grid:
            for cell in row:
                cell.visited = False

    def get_neighbors(self, cell: Cell) -> List[Tuple[Direction, Cell]]:
        """Return all valid adjacent cells"""
        neighbors: List[Tuple[Direction, Cell]] = []

        for direction in Direction:
            dx, dy = direction.delta()
            nx = cell.x + dx
            ny = cell.y + dy

            if self.in_bounds(nx, ny):
                neighbor = self.get_cell(nx, ny)
                neighbors.append((direction, neighbor))

        return neighbors

    def remove_wall_between(
        self, cell: Cell, neighbor: Cell, direction: Direction
    ) -> None:
        """Remove walls between two adjacent cells in the given direction."""
        cell.remove_wall(direction)
        neighbor.remove_wall(direction.opposite())

    def save_maze(self, filename: str, path_str: str) -> None:
        """
        Saves the maze in the hex-encoded format required by the subject.
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for y in range(self.height):
                    row_hex = ""
                    for x in range(self.width):
                        cell = self.get_cell(x, y)
                        row_hex += format(cell.walls, "X")
                    f.write(row_hex + "\n")

                f.write("\n")

                f.write(f"{self.entry[0]},{self.entry[1]}\n")

                f.write(f"{self.exit[0]},{self.exit[1]}\n")

                f.write(f"{path_str}\n")

            print(f"Successfully exported to {filename}")
        except Exception as e:
            print(f"Error saving output file: {e}")


def print_maze(
    maze: Maze,
    path: str = "",
    show_path: bool = True,
    wall_color: str = "\033[42m",
    animate: bool = False,
    msg: bool = False,
) -> None:
    """
    Visual representation of the maze for the terminal.
    Shows walls, entry, exit, the solution path, and the '42' pattern.
    """
    RESET = "\033[0m"
    WALL = f"{wall_color}  {RESET}"
    CELL_42 = "\033[41m  \033[0m"
    PATH = "\033[44m  \033[0m"
    EMPTY = "  "
    START = "\033[45m  \033[0m"
    END = "\033[41m  \033[0m"

    h_canvas, w_canvas = maze.height * 2 + 1, maze.width * 2 + 1
    canvas = [[WALL for _ in range(w_canvas)] for _ in range(h_canvas)]
    cells_42: Set[Tuple[int, int]] = maze.cells_42
    for y in range(maze.height):
        for x in range(maze.width):
            cell = maze.get_cell(x, y)
            cy, cx = y * 2 + 1, x * 2 + 1

            if (x, y) in cells_42:
                canvas[cy][cx] = CELL_42
                for d in (Direction.N, Direction.E, Direction.S, Direction.W):
                    if not cell.has_wall(d):
                        dx, dy = d.delta()
                        canvas[cy + dy][cx + dx] = CELL_42
            else:
                canvas[cy][cx] = EMPTY
                for d in (Direction.N, Direction.E, Direction.S, Direction.W):
                    if not cell.has_wall(d):
                        dx, dy = d.delta()
                        canvas[cy + dy][cx + dx] = EMPTY

    path_coords: List[Tuple[int, int]] = []
    if path:
        curr_x, curr_y = maze.entry
        path_coords.append((curr_x, curr_y))
        for move in path:
            d = Direction[move]
            dx, dy = d.delta()
            curr_x, curr_y = curr_x + dx, curr_y + dy
            path_coords.append((curr_x, curr_y))

    def render(step: Optional[int] = None) -> None:
        print("\033[H\033[J", end="")
        for y in range(h_canvas):
            for x in range(w_canvas):
                if y % 2 == 1 and x % 2 == 1:
                    mx, my = x // 2, y // 2
                    if (mx, my) == maze.entry:
                        print(START, end="")
                        continue
                    if (mx, my) == maze.exit:
                        print(END, end="")
                        continue
                    if (mx, my) in cells_42:
                        print(CELL_42, end="")
                        continue
                    if show_path and path_coords:
                        limit = step if step is not None else len(path_coords)
                        if (mx, my) in path_coords[:limit]:
                            print(PATH, end="")
                            continue
                print(canvas[y][x], end="")
            print()
        print()
        if msg:
            print("Maze too small for '42' pattern.")

    if animate and show_path:
        for i in range(1, len(path_coords) + 1):
            render(i)
            time.sleep(0.05)
    else:
        render()
