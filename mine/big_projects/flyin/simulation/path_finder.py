from simulation.graph_builder import GraphBuilder
from typing import List, Dict, Tuple
from simulation.algo import Algo
from model.zone import Zone


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
            self.start.name,
            self.end.name,
            [(self.start.name, 0)],
            set(),
            all_paths
        )
        return self.sort_by_cost(all_paths)

    def get_zone_by_name(self, zone_name: str) -> Zone:
        for zone in self.zones:
            if zone.name == zone_name:
                return zone
        return None

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

        unc_paths = [path[0] for path in sorted_lst]
        clear_paths = self.extract_path(unc_paths)

        zone_paths = []
        for path in clear_paths:
            lst_zones = []
            for zone in path:
                z = self.get_zone_by_name(zone)
                lst_zones.append(z)
            zone_paths.append(lst_zones)
        return (zone_paths)

    def extract_path(self, old_path):
        new_paths = []
        for path in old_path:
            lst = []
            for item in path:
                lst.append(item[0])
            new_paths.append(lst)
        return new_paths
