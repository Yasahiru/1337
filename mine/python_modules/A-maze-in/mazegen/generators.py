import random
from typing import List, Tuple, Set, Optional, Dict
from collections import deque
from .display_class import Maze
from .cell_class import Cell
from .direction_class import Direction, ALL_DIRECTIONS

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
ParentMap = Dict[Tuple[int, int], Optional[Tuple[Tuple[int, int], Direction]]]


class MazeGenerator:
    """Encapsulates maze generation (DFS / Prim) with '42' stamping."""

    def __init__(self, maze: Maze, seed: Optional[int] = None) -> None:
        self.maze = maze
        if seed is not None:
            random.seed(seed)

    def generate(self, algorithm: str, perfect: bool) -> bool:
        """Generate a maze using the selected algorithm."""
        self._validate()
        stamp_successful = self._stamp_42()
        if algorithm == "DFS":
            self.generate_dfs()
        elif algorithm == "PRIM":
            self.generate_prim()
        else:
            raise ValueError(
                f"Unknown algorithm '{algorithm}'." " Expected 'DFS' or 'PRIM'"
            )
        if not perfect:
            self.add_imperfections()
        return not stamp_successful

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
        frontier: list[tuple[Cell, Cell, Direction]] = []
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

    def _stamp_42(self) -> bool:
        """Mark '42' cells as visited walls so generators route around them."""
        if self.maze.width < 9 or self.maze.height < 9:
            self.maze.cells_42 = set()
            return False

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
        return True

    def add_imperfections(self, rate: float = 0.2) -> None:
        """Randomly removes walls to make the maze imperfect."""
        maze = self.maze
        protected: Set[Tuple[int, int]] = getattr(maze, "cells_42", set())

        for y in range(maze.height):
            for x in range(maze.width):
                cell = maze.get_cell(x, y)

                if (x, y) in protected:
                    continue

                for _dir in (
                    Direction.N,
                    Direction.E,
                    Direction.S,
                    Direction.W,
                ):
                    dx, dy = _dir.delta()
                    nx, ny = x + dx, y + dy

                    if not maze.in_bounds(nx, ny):
                        continue

                    if (nx, ny) in protected:
                        continue

                    nei = maze.get_cell(nx, ny)

                    if cell.has_wall(_dir):
                        if cell.visited and nei.visited:
                            if random.random() < rate:
                                if not self._creates_open_area_3x3(
                                    maze,
                                    x,
                                    y,
                                    _dir
                                ):
                                    maze.remove_wall_between(cell, nei, _dir)

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

    def solve(self, maze: Maze) -> str:
        start = maze.entry
        goal = maze.exit
        queue = deque([start])

        # type hint:
        # Dict[Tuple[int, int], Optional[Tuple[Tuple[int, int], Direction]]]
        parent: ParentMap = {start: None}
        while queue:
            x, y = queue.popleft()
            if (x, y) == goal:
                return self._reconstruct_path(parent, goal)
            cell = maze.get_cell(x, y)
            for direction in Direction:
                if direction.name == "ALL":
                    continue
                if cell.has_wall(direction):
                    continue
                dx, dy = direction.delta()
                nx, ny = x + dx, y + dy
                if not maze.in_bounds(nx, ny):
                    continue
                if (nx, ny) in parent:
                    continue
                parent[(nx, ny)] = ((x, y), direction)
                queue.append((nx, ny))
        raise ValueError("No path found from entry to exit")

    def _reconstruct_path(
        self,
        parent: ParentMap,
        goal: Tuple[int, int],
    ) -> str:
        path: List[str] = []
        current = goal

        while parent[current] is not None:
            entry = parent.get(current)
            if entry is None:
                break
            prev, direction = entry
            path.append(direction.name)
            current = prev
        path.reverse()
        return "".join(path)
