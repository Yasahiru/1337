from collections import deque
from typing import Dict, Tuple, List, Optional

from srcs.display_class import Maze
from srcs.direction_class import Direction


ParentMap = Dict[
    Tuple[int, int],
    Optional[Tuple[Tuple[int, int], Direction]]
]


class MazeSolver:
    """
    Solves the maze using BFS (shortest path).
    Returns path as a string of directions: NESW
    """

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
