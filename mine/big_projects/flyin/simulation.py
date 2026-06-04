from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Dict, List, Optional, Set, Tuple

from model.connection import Connection
from model.zone import Zone
from model.zone_type import ZoneType
from parser.parser import Parser
from parser.validator import Validator


@dataclass
class SimDrone:
    drone_id: int
    current_zone: Zone
    path: List[Zone]
    path_index: int = 1
    in_transit_connection: Optional[Connection] = None
    target_zone: Optional[Zone] = None
    turns_left: int = 0
    delivered: bool = False

    def next_zone(self) -> Optional[Zone]:
        if self.path_index >= len(self.path):
            return None
        return self.path[self.path_index]

    def advance_path(self) -> None:
        self.path_index += 1

    def is_in_transit(self) -> bool:
        return self.in_transit_connection is not None


class Simulator:
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        self.zones_by_name: Dict[str, Zone] = {}
        self.connections: List[Connection] = []
        self.start_zone: Optional[Zone] = None
        self.end_zone: Optional[Zone] = None
        self.drones: List[SimDrone] = []
        self.adjacency: Dict[str, List[Connection]] = {}

    def load(self) -> None:
        parser = Parser(self.file_path)
        parser.load()

        validator = Validator(parser.zones, parser.connections)
        zones = validator.zones_obj()

        zone_kind: Dict[str, str] = {
            zone_dict["name"]: zone_dict["kind"]
            for zone_dict in parser.zones
        }

        self.zones_by_name = {zone.name: zone for zone in zones}
        self.start_zone = self._find_zone_by_kind(
            zone_kind,
            "start_hub",
        )
        self.end_zone = self._find_zone_by_kind(
            zone_kind,
            "end_hub",
        )
        self.connections = self._build_connections(parser.connections)
        self.adjacency = self._build_adjacency()
        self._build_drone_objects(parser.nb_drones)

    def _find_zone_by_kind(self, kind_map: Dict[str, str], kind: str) -> Zone:
        for zone_name, zone_kind in kind_map.items():
            if zone_kind == kind:
                return self.zones_by_name[zone_name]
        raise ValueError(f"Missing required zone of kind {kind}")

    def _build_connections(
        self,
        raw_connections: List[Dict[str, object]],
    ) -> List[Connection]:
        connections: List[Connection] = []
        for raw in raw_connections:
            zone1 = self.zones_by_name[raw["zone1"]]
            zone2 = self.zones_by_name[raw["zone2"]]
            metadata = raw["meta_data"]
            max_link_capacity = int(metadata.get("max_link_capacity", 1))
            connection = Connection(
                zone1=zone1,
                zone2=zone2,
                max_link_capacity=max_link_capacity,
            )
            connections.append(connection)
        return connections

    def _build_adjacency(self) -> Dict[str, List[Connection]]:
        adjacency: Dict[str, List[Connection]] = {
            name: [] for name in self.zones_by_name
        }
        for connection in self.connections:
            adjacency[connection.zone1.name].append(connection)
            adjacency[connection.zone2.name].append(connection)
        return adjacency

    def _build_drone_objects(self, nb_drones: int) -> None:
        if self.start_zone is None or self.end_zone is None:
            raise ValueError("Start zone or end zone is missing")

        path_options = self._find_path_options()
        if not path_options:
            raise ValueError("No valid paths from start to end")

        self.start_zone.current_drones = []
        self.drones = []

        for drone_id in range(1, nb_drones + 1):
            drone = SimDrone(
                drone_id=drone_id,
                current_zone=self.start_zone,
                path=self._choose_path_for_drone(
                    drone_id,
                    path_options,
                ),
            )
            self.drones.append(drone)
            self.start_zone.current_drones.append(drone)

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

    def _choose_path_for_drone(
        self,
        drone_id: int,
        paths: List[List[Zone]],
    ) -> List[Zone]:
        if not paths:
            raise ValueError("No paths available for drone assignment")
        return paths[(drone_id - 1) % len(paths)]

    def _path_sort_key(self, path: List[Zone]) -> Tuple[int, int]:
        return (self._path_cost(path), len(path))

    def _path_cost(self, path: List[Zone]) -> int:
        return sum(self._zone_cost(zone) for zone in path[1:])

    def _zone_cost(self, zone: Zone) -> int:
        return 2 if zone.zone_type == ZoneType.RESTRICTED else 1

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

    def _find_connection(
        self,
        from_zone: Zone,
        to_zone: Zone,
    ) -> Optional[Connection]:
        for connection in self.adjacency[from_zone.name]:
            if connection.zone1 is to_zone or connection.zone2 is to_zone:
                return connection
        return None

    def _connection_name(self, connection: Connection) -> str:
        return f"{connection.zone1.name}-{connection.zone2.name}"



    def run(self) -> tuple[List[str], int]:
        if self.start_zone is None or self.end_zone is None:
            raise ValueError("Simulator not loaded")

        lines: List[str] = []
        max_turns = 1000
        turn_count = 0

        while max_turns > 0:
            all_delivered = all(drone.delivered for drone in self.drones)
            if all_delivered:
                break
            max_turns -= 1
            turn_count += 1
            turn_moves: List[str] = []

            for drone in self.drones:
                if drone.is_in_transit():
                    drone.turns_left -= 1
                    if drone.turns_left <= 0 and drone.target_zone is not None:
                        transit_conn = drone.in_transit_connection
                        connection_list = transit_conn.current_drones
                        if drone in connection_list:
                            connection_list.remove(drone)
                        drone.current_zone = drone.target_zone
                        drone.current_zone.current_drones.append(drone)
                        drone.advance_path()
                        drone.target_zone = None
                        drone.in_transit_connection = None
                        if drone.current_zone is self.end_zone:
                            drone.delivered = True
                    else:
                        transit_conn = drone.in_transit_connection
                        connection_name = self._connection_name(transit_conn)
                        turn_moves.append(
                            f"D{drone.drone_id}-{connection_name}"
                        )

            for drone in self.drones:
                if drone.delivered or drone.is_in_transit():
                    continue
                if drone.current_zone is self.end_zone:
                    drone.delivered = True
                    continue
                next_zone = drone.next_zone()
                if next_zone is None:
                    continue
                connection = self._find_connection(
                    drone.current_zone,
                    next_zone,
                )
                if connection is None:
                    continue
                current_drone_count = len(connection.current_drones)
                if current_drone_count >= connection.max_link_capacity:
                    continue
                if (
                    next_zone is not self.end_zone
                    and len(next_zone.current_drones) >= next_zone.max_drones
                ):
                    continue

                connection.current_drones.append(drone)
                if next_zone.zone_type == ZoneType.RESTRICTED:
                    if drone in drone.current_zone.current_drones:
                        drone.current_zone.current_drones.remove(drone)
                    drone.in_transit_connection = connection
                    drone.target_zone = next_zone
                    drone.turns_left = 2
                    connection_name = self._connection_name(connection)
                    turn_moves.append(
                        f"D{drone.drone_id}-{connection_name}"
                    )
                else:
                    if drone in drone.current_zone.current_drones:
                        drone.current_zone.current_drones.remove(drone)
                    next_zone.current_drones.append(drone)
                    drone.current_zone = next_zone
                    drone.advance_path()
                    turn_moves.append(
                        f"D{drone.drone_id}-{next_zone.name}"
                    )
                    if drone in connection.current_drones:
                        connection.current_drones.remove(drone)
                    if next_zone is self.end_zone:
                        drone.delivered = True

            if turn_moves:
                lines.append(" ".join(turn_moves))

        if max_turns <= 0:
            raise RuntimeError("Simulation did not finish in time")

        return lines, turn_count


def run_simulation(file_path: str) -> tuple[List[str], int]:
    simulator = Simulator(file_path)
    simulator.load()
    return simulator.run()


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python simulation.py <map file>")
        sys.exit(1)

    result_lines = run_simulation(sys.argv[1])
    for line in result_lines:
        print(line)
