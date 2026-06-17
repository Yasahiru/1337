from model.drone import Drone
from model.drone_state import DroneState
from model.zone import Zone


class Simulator:
    def __init__(self, start, nb_drones, paths, zones, conns, graph) -> None:
        self.nb_drones = nb_drones
        self.start = start
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
        unique_paths = min(len(self.drones), len(self.paths))

        for i, drone in enumerate(self.drones):
            path_idx = i % unique_paths
            drone.assigned_path = self.paths[path_idx]
            drone.current_location = drone.assigned_path[0]

        return self.drones

    def get_next_zone(self, drone: Drone) -> Zone:
        next_zone = 0
        if drone.path_index != len(drone.assigned_path):
            new_idx = drone.path_index + 1
            next_zone = drone.assigned_path[new_idx]
        else:
            next_zone = None
        return next_zone

    def run(self):
        return self.conns

    def get_output():
        ...
