from model.drone import Drone
from model.drone_state import DroneState


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
        num_drones = len(self.drones)
        num_paths = len(self.paths)
        num_unique_paths = min(num_drones, num_paths)
        selected_paths = self.paths[:num_unique_paths]

        assigned_drones = []
        for i, drone in enumerate(self.drones):
            path_idx = i % num_unique_paths
            selected_path = selected_paths[path_idx]

            drone.assigned_path = selected_path
            drone.current_location = selected_path[0][0]
            drone.path_index = 0
            drone.start_turn = i

            assigned_drones.append(drone)
        return assigned_drones

    def run():
        ...

    def get_output():
        ...
