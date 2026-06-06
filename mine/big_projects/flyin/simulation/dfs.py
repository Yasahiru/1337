from typing import List, Set
from model.zone import Zone
from model.zone_type import ZoneType


def _find_path_options(self, max_paths: int = 3) -> List[List[Zone]]:
    if self.start_zone is None or self.end_zone is None:
        raise ValueError("Missing start or end zone")

    paths: List[List[Zone]] = []
    visited: Set[str] = {self.start_zone.name}

    self._collect_candidate_paths(
        self.start_zone,
        visited,
        [self.start_zone],
        paths,
        max_paths,
    )
    return sorted(paths, key=self._path_sort_key)[:max_paths]


def _collect_candidate_paths(
    self,
    current_zone: Zone,
    visited: Set[str],
    path: List[Zone],
    results: List[List[Zone]],
    max_paths: int,
) -> None:
    if len(results) >= max_paths:
        return

    if current_zone is self.end_zone:
        results.append(path.copy())
        return

    next_zones: List[tuple[int, str, Zone]] = []

    for connection in self.adjacency[current_zone.name]:
        next_zone = (
            connection.zone2
            if connection.zone1 is current_zone
            else connection.zone1
        )

        if next_zone.name in visited:
            continue

        if next_zone.zone_type == ZoneType.BLOCKED:
            continue

        next_zones.append(
            (self._zone_cost(next_zone), next_zone.name, next_zone)
        )

    next_zones.sort(key=lambda item: (item[0], item[1]))

    for _, _, next_zone in next_zones:
        visited.add(next_zone.name)
        path.append(next_zone)

        self._collect_candidate_paths(
            next_zone,
            visited,
            path,
            results,
            max_paths,
        )

        path.pop()
        visited.remove(next_zone.name)
