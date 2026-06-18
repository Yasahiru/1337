from model.drone import Drone
from model.drone_state import DroneState
from model.zone import Zone
from model.connection import Connection


class Simulator:
    def __init__(
        self, start, end, nb_drones, paths, zones, conns, graph
    ) -> None:
        self.nb_drones = nb_drones
        self.start = start
        self.end = end
        self.paths = paths
        self.zones = zones
        self.conns = conns
        self.graph = graph
        self.drones = []

    def create_drones(self) -> None:
        for i in range(self.nb_drones):
            drone = Drone(
                drone_id=f"D{i+1}",
                current_location=self.start,
                state=DroneState.WAITING
            )
            self.drones.append(drone)

    def assign_drones_to_paths(self):
        if not self.paths:
            raise ValueError("No valid paths found.")

        unique_paths = min(len(self.drones), len(self.paths))
        for i, drone in enumerate(self.drones):
            path_idx = i % unique_paths
            drone.assigned_path = self.paths[path_idx]
            drone.current_location = drone.assigned_path[0]

        return self.drones

    def get_next_zone(self, drone: Drone) -> Zone:
        next_idx = drone.path_index + 1
        if next_idx >= len(drone.assigned_path):
            return None
        return drone.assigned_path[next_idx]

    def find_connection(self, zone: Zone, dest: Zone) -> Connection:
        for conn in self.conns:
            if conn.zone1 == zone or conn.zone2 == zone:
                if conn.zone2 == dest:
                    return conn
                if conn.zone1 == dest:
                    return conn
        return None

    def can_drone_move(self, drone: Drone) -> bool:
        next_zone = self.get_next_zone(drone)
        if not next_zone:
            return False
        if drone.is_delivered:
            return False

        connection = self.find_connection(drone.current_location, next_zone)

        if not connection:
            return False

        current_drones = len(connection.current_drones)
        if current_drones >= connection.max_link_capacity:
            return False

        if next_zone != self.end:
            if len(next_zone.current_drones) >= next_zone.max_drones:
                return False

        return (True)

    # to be continued:
    def run(self):
        return self.conns

    def get_output():
        ...
