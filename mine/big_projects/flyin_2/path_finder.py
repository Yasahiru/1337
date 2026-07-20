from graph_builder import GraphBuilder
from typing import Dict, List, Optional, Tuple
from connection import Connection
from algo import Algo
from zone_model import Zone


class PathFinder:
    def __init__(
        self,
        zones: List[Zone],
        conns: List[Connection],
        start: Zone,
        end: Zone,
    ) -> None:
        self.zones: List[Zone] = zones
        self.conns: List[Connection] = conns
        self.start: Zone = start
        self.end: Zone = end
        self.graph: Dict[str, List[Tuple[str, int]]] = {}
        self.paths: List[List[Zone]] = []

    def load(self) -> None:
        gbuild = GraphBuilder(self.zones, self.conns)
        self.graph = gbuild.build_graph()

    def get_multiple_paths(self) -> List[List[Zone]]:
        self.load()

        algo = Algo(
            self.zones,
            self.graph,
        )

        all_paths: List[List[Tuple[str, int]]] = []

        algo.dfs(
            self.start.name,
            self.end.name,
            [(self.start.name, 0)],
            set(),
            all_paths
        )
        return self.sort_by_cost(all_paths)

    def get_zone_by_name(self, zone_name: str) -> Optional[Zone]:
        for zone in self.zones:
            if zone.name == zone_name:
                return zone
        return None

    def sort_by_cost(
        self,
        all_paths: List[List[Tuple[str, int]]],
    ) -> List[List[Zone]]:
        new_lst: List[Tuple[List[Tuple[str, int]], int]] = []
        for path_list in all_paths:
            cost = 0
            for path_entry in path_list:
                cost += path_entry[1]
            new_lst.append((path_list, cost))

        sorted_lst: List[Tuple[List[Tuple[str, int]], int]] = sorted(
            new_lst,
            key=lambda x: x[1]
        )

        unc_paths: List[List[Tuple[str, int]]] = []
        for path_info in sorted_lst:
            path_list, _cost = path_info
            unc_paths.append(path_list)
        path_strings: List[List[str]] = []
        for path_list in unc_paths:
            string_path: List[str] = []
            for item in path_list:
                string_path.append(item[0])
            path_strings.append(string_path)

        zone_paths: List[List[Zone]] = []
        for path in path_strings:
            lst_zones: List[Zone] = []
            for zone_name in path:
                z = self.get_zone_by_name(zone_name)
                if z is None:
                    raise ValueError(f"Unknown zone '{zone_name}' in path")
                lst_zones.append(z)
            zone_paths.append(lst_zones)
        return (zone_paths)

    def extract_path(
        self,
        old_path: List[List[Tuple[str, int]]],
    ) -> List[List[str]]:
        new_paths: List[List[str]] = []
        for path in old_path:
            lst: List[str] = []
            for item in path:
                lst.append(item[0])
            new_paths.append(lst)
        return new_paths
