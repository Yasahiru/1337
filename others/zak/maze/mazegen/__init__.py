"""Mazegen - A reusable maze generation package.

This package provides a maze generator using the recursive backtracker
algorithm, along with a BFS-based pathfinder to solve the generated maze.

Example:
    from mazegen import MazeGenerator

    maze = MazeGenerator(
        width=20,
        height=15,
        seed=42,
        perfect=True,
        entry_point=(0, 0),
        exit_point=(19, 14)
    )

    solution = maze.solve()
    print(solution)
"""

from mazegen.generator import MazeGenerator
from mazegen.writer import MazeWriter

__all__ = ["MazeGenerator", "MazeWriter"]
