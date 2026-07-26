from typing import Dict, List, Set, Tuple
from zone_model import Zone


class Algo:

    def __init__(
        self,
        zones: List[Zone],
        graph: Dict[str, List[Tuple[str, int]]],
    ) -> None:
        self.zones = zones
        self.graph = graph
        self.distances: Dict[str, float] = {}
        self.previous: Dict[str, str | None] = {}
        self.unvisited: Set[str] = set()

    def dfs(
        self,
        current: str,
        target: str,
        path: List[Tuple[str, int]],
        visited: Set[str],
        all_paths: List[List[Tuple[str, int]]],
    ) -> None:
        if current == target:
            all_paths.append(path.copy())
            return

        visited.add(current)
        nei = self.graph[current]

        for name, weight in nei:
            if name not in visited:
                path.append((name, weight))
                self.dfs(name, target, path, visited, all_paths)
                path.pop()

        visited.remove(current)
