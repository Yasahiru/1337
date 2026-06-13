from simulation.graph_builder import GraphBuilder
from typing import List, Dict, Tuple
from simulation.dijkstra import Algo


class PathFinder:
    def __init__(self, zones, conns, start, end) -> None:
        self.zones = zones
        self.conns = conns
        self.start = start
        self.end = end
        self.graph: Dict = {}
        self.paths: List[List[str]] = []

    def load(self):
        gbuild = GraphBuilder(self.zones, self.conns)
        self.graph = gbuild.build_graph()

    def get_multiple_paths(self) -> list[List[str]]:
        self.load()
        algo = Algo(
            self.zones,
            self.graph,
        )
        all_paths = []
        algo.dfs(
            self.start,
            self.end,
            [(self.start, 0)],
            set(),
            all_paths
        )
        return self.sort_by_cost(all_paths)

    def sort_by_cost(self, all_paths) -> List[Tuple[List, int]]:
        new_lst = []
        for path in all_paths:
            cost = 0
            for z in path:
                cost += z[1]
            new_lst.append((path, cost))
        sorted_lst = sorted(
            new_lst,
            key=lambda x: x[1]
        )
        return self.extract_path(sorted_lst)

    def extract_path(self, old_path):
        return [
            item[0] if isinstance(item, tuple) else item for item in old_path
        ]
