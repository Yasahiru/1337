from typing import List, Dict, Optional
from model.zone import Zone
from model.zone_type import ZoneType
from heapq import heappop, heappush


def _find_path(self) -> List[Zone]:

    if self.start_zone is None or self.end_zone is None:
        raise ValueError("Missing start or end zone")

    distances: Dict[str, int] = {
        name: float("inf") for name in self.zones_by_name
    }

    previous: Dict[str, Optional[str]] = {
        name: None for name in self.zones_by_name
    }

    distances[self.start_zone.name] = 0
    queue: List[tuple[int, str]] = [(0, self.start_zone.name)]

    while queue:
        current_cost, current_name = heappop(queue)

        if current_cost > distances[current_name]:
            continue

        if current_name == self.end_zone.name:
            break

        for connection in self.adjacency[current_name]:

            if connection.zone1.name == current_name:
                next_zone = connection.zone2
            else:
                next_zone = connection.zone1

            if next_zone.zone_type == ZoneType.BLOCKED:
                continue

            cost = 2 if next_zone.zone_type == ZoneType.RESTRICTED else 1
            next_cost = current_cost + cost

            if next_cost < distances[next_zone.name]:
                distances[next_zone.name] = next_cost
                previous[next_zone.name] = current_name
                heappush(queue, (next_cost, next_zone.name))

    if previous[self.end_zone.name] is None:
        return []

    path_names: List[str] = []
    current = self.end_zone.name

    while current is not None:
        path_names.insert(0, current)
        current = previous[current]

    return [self.zones_by_name[name] for name in path_names]
