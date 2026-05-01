import random
from typing import List, Tuple, Set
from srcs.display_class import Maze
from srcs.cell_class import Cell
from srcs.direction_class import Direction, ALL_DIRECTIONS

DIGIT_4 = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 1],
]
DIGIT_2 = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1],
]

DIGIT_H, DIGIT_W, GAP = 5, 3, 1
PATTERN_W = DIGIT_W + GAP + DIGIT_W


class MazeGenerator:
    """Encapsulates maze generation (DFS / Prim) with '42' stamping."""

    def __init__(self, maze: Maze, seed: int = None):
        self.maze = maze
        if seed is not None:
            random.seed(seed)

    def _validate(self) -> None:
        """Validate maze parameters before generation."""
        if self.maze.width <= 0 or self.maze.height <= 0:
            raise ValueError(
                f"Maze dimensions must be positive, got "
                f"{self.maze.width}x{self.maze.height}"
            )

        ex, ey = self.maze.entry
        if not self.maze.in_bounds(ex, ey):
            raise ValueError(
                f"Entry {self.maze.entry} is outside the maze bounds "
                f"({self.maze.width}x{self.maze.height})"
            )

        xx, xy = self.maze.exit
        if not self.maze.in_bounds(xx, xy):
            raise ValueError(
                f"Exit {self.maze.exit} is outside the maze bounds "
                f"({self.maze.width}x{self.maze.height})"
            )

        if self.maze.entry == self.maze.exit:
            raise ValueError("Entry and exit cannot be the same cell")

    def generate(self, algorithm: str, perfect: bool) -> None:
        """Generate a maze using the selected algorithm."""
        self._validate()
        self._stamp_42()
        if algorithm == "DFS":
            self.generate_dfs()
        elif algorithm == "PRIM":
            self.generate_prim()
        else:
            raise ValueError(
                f"Unknown algorithm '{algorithm}'." " Expected 'DFS' or 'PRIM'."
            )
        if not perfect:
            self.add_imperfections()

    def generate_dfs(self) -> None:
        """Generate maze using DFS algorithm."""
        stack = [self.maze.get_cell(0, 0)]
        stack[0].visited = True

        while stack:
            current = stack[-1]
            neighbors = self.unvisited_neighbors(current, maze=self.maze)
            if neighbors:
                d, nxt = random.choice(neighbors)
                self.maze.remove_wall_between(current, nxt, d)
                nxt.visited = True
                stack.append(nxt)
            else:
                stack.pop()

    def generate_prim(self) -> None:
        """Generate maze using Prim algorithm."""
        start_cell = self.maze.get_cell(0, 0)
        start_cell.visited = True

        frontier = []
        for direction, neighbor in self.maze.get_neighbors(start_cell):
            frontier.append((start_cell, neighbor, direction))

        while frontier:
            random_index = random.randrange(len(frontier))
            current, neighbor, wall_dir = frontier.pop(random_index)

            if neighbor.visited:
                continue

            self.maze.remove_wall_between(current, neighbor, wall_dir)
            neighbor.visited = True

            for next_dir, next_neighbor in self.maze.get_neighbors(neighbor):
                if not next_neighbor.visited:
                    frontier.append((neighbor, next_neighbor, next_dir))

    def unvisited_neighbors(
        self, cell: Cell, maze: Maze
    ) -> List[Tuple[Direction, Cell]]:
        neighbors = maze.get_neighbors(cell)
        result = []

        for direction, neighbor in neighbors:
            if not neighbor.visited:
                result.append((direction, neighbor))

        return result

    def _stamp_42(self) -> None:
        """Mark '42' cells as visited walls so generators route around them."""
        if self.maze.width < 9 or self.maze.height < 9:
            print("Maze too small for '42' pattern.")
            self.maze.cells_42 = set()
            return

        start = (self.maze.width - PATTERN_W) // 2
        begin = (self.maze.height - DIGIT_H) // 2

        cells_42: Set[Tuple[int, int]] = set()
        for row in range(DIGIT_H):
            for col in range(DIGIT_W):
                if DIGIT_4[row][col]:
                    cells_42.add((start + col, begin + row))
                if DIGIT_2[row][col]:
                    cells_42.add((start + DIGIT_W + GAP + col, begin + row))
        self.maze.cells_42 = cells_42

        for x, y in cells_42:
            cell = self.maze.get_cell(x, y)
            cell.walls = ALL_DIRECTIONS
            cell.visited = True

        for x, y in cells_42:
            for d in (Direction.N, Direction.E, Direction.S, Direction.W):
                dx, dy = d.delta()
                if (x + dx, y + dy) in cells_42:
                    self.maze.get_cell(x, y).remove_wall(d)

        for x, y in cells_42:
            for d in (Direction.N, Direction.E, Direction.S, Direction.W):
                dx, dy = d.delta()
                nx, ny = x + dx, y + dy
                if self.maze.in_bounds(nx, ny) and (nx, ny) not in cells_42:
                    self.maze.get_cell(nx, ny).add_wall(d.opposite())

    def add_imperfections(self, rate: float = 0.2) -> None:
        """Randomly removes walls to make the maze imperfect."""
        maze = self.maze
        protected = getattr(maze, "cells_42", set())

        for y in range(maze.height):
            for x in range(maze.width):
                cell = maze.get_cell(x, y)

                if (x, y) in protected:
                    continue

                for direction in (
                    Direction.N,
                    Direction.E,
                    Direction.S,
                    Direction.W,
                ):
                    dx, dy = direction.delta()
                    nx, ny = x + dx, y + dy

                    if not maze.in_bounds(nx, ny):
                        continue

                    if (nx, ny) in protected:
                        continue

                    neighbor = maze.get_cell(nx, ny)

                    if cell.has_wall(direction) and cell.visited and neighbor.visited:
                        if random.random() < rate:
                            if not self._creates_open_area_3x3(maze, x, y, direction):
                                maze.remove_wall_between(cell, neighbor, direction)

    def _creates_open_area_3x3(
        self, maze: Maze, x: int, y: int, direction: Direction
    ) -> bool:
        test_cells = []
        for yy in range(y - 1, y + 2):
            for xx in range(x - 1, x + 2):
                if maze.in_bounds(xx, yy):
                    test_cells.append((xx, yy))
        open_count = 0
        for cx, cy in test_cells:
            cell = maze.get_cell(cx, cy)
            walls = 0
            for d in (Direction.N, Direction.E, Direction.S, Direction.W):
                if cell.has_wall(d):
                    walls += 1
            if walls <= 1:
                open_count += 1
        return open_count >= 6

    def save_maze(self, filename: str, path_str: str) -> None:
        """
        Saves the maze in the hex-encoded format required by the subject.
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for y in range(self.maze.height):
                    row_hex = ""
                    for x in range(self.maze.width):
                        cell = self.maze.get_cell(x, y)
                        row_hex += format(cell.walls, "X")
                    f.write(row_hex + "\n")

                f.write("\n")

                f.write(f"{self.maze.entry[0]},{self.maze.entry[1]}\n")

                f.write(f"{self.maze.exit[0]},{self.maze.exit[1]}\n")

                f.write(f"{path_str}\n")

            print(f"Successfully exported to {filename}")
        except Exception as e:
            print(f"Error saving output file: {e}")
