from typing import Dict, List, Optional, Set, Tuple
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

    def load(self, start: str) -> None:
        for z in self.zones:
            self.distances[z.name] = float("inf")
            self.previous[z.name] = None

        self.distances[start] = 0
        self.unvisited = set(self.graph.keys())

    def get_min_unvisited(self) -> Optional[str]:
        mine_zone: Optional[str] = None
        min_dist = float("inf")

        for z in self.unvisited:
            if self.distances[z] < min_dist:
                min_dist = self.distances[z]
                mine_zone = z
        return mine_zone

    def relax(self, current: str) -> None:
        cur = self.graph[current]
        for el in cur:
            neigh = el[0]
            dest = el[1]
            new_dest = self.distances[current] + dest
            if new_dest < self.distances[neigh]:
                self.distances[neigh] = new_dest
                self.previous[neigh] = current

    def run(self, start: str) -> None:
        self.load(start)
        while self.unvisited:
            current = self.get_min_unvisited()
            if current is None or self.distances[current] == float("inf"):
                break
            self.relax(current)
            self.unvisited.remove(current)

    def get_path(self, end: str) -> List[str]:
        path: List[str] = []
        zone: str | None = end
        while zone:
            path.append(zone)
            zone = self.previous[zone]

        path.reverse()
        return (path)

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
