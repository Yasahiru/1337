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
        zone_names = [zone_name for zone_name, weight in self.path]
        [zone_names]

    def run():
        ...

    def get_output():
        ...
