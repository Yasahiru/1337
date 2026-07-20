from drone import Drone
from zone_model import Zone
from zone_type import ZoneType
from connection import Connection
from typing import Dict, List, Optional, Union


class Simulator:
    def __init__(
        self,
        start: Zone,
        end: Zone,
        nb_drones: int,
        paths: List[List[Zone]],
        zones: List[Zone],
        conns: List[Connection],
        graph: Dict[str, List[tuple[str, int]]],
    ) -> None:
        self.nb_drones: int = nb_drones
        self.start: Zone = start
        self.end: Zone = end
        self.paths: List[List[Zone]] = paths
        self.zones: List[Zone] = zones
        self.conns: List[Connection] = conns
        self.graph: Dict[str, List[tuple[str, int]]] = graph
        self.drones: List[Drone] = []
        self.turn_logs: List[str] = []
        self.frames: List[Dict[str, Union[Zone, Connection]]] = []

    ANSI_COLORS: dict[str, str] = {
        # Standard ANSI
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",

        # Bright ANSI
        "gray": "\033[90m",
        "light_red": "\033[91m",
        "light_green": "\033[92m",
        "light_yellow": "\033[93m",
        "light_blue": "\033[94m",
        "light_magenta": "\033[95m",
        "light_cyan": "\033[96m",

        # Colors seen in your maps
        "orange": "\033[38;5;214m",
        "purple": "\033[38;5;129m",
        "brown": "\033[38;5;94m",
        "maroon": "\033[38;5;52m",
        "gold": "\033[38;5;220m",
        "darkred": "\033[38;5;88m",
        "crimson": "\033[38;5;160m",
        "violet": "\033[38;5;177m",

        # Common extras
        "pink": "\033[38;5;213m",
        "navy": "\033[38;5;18m",
        "teal": "\033[38;5;30m",
        "lime": "\033[38;5;118m",
        "olive": "\033[38;5;100m",
        "turquoise": "\033[38;5;44m",
        "indigo": "\033[38;5;54m",
        "coral": "\033[38;5;209m",
        "salmon": "\033[38;5;216m",
        "beige": "\033[38;5;230m",
        "silver": "\033[38;5;250m",
        "aqua": "\033[38;5;51m",

        # Special/fun names
        "rainbow": "\033[38;5;51m",
    }
    DEFAULT_COLOR = "\033[37m"  # white as default
    RESET = "\033[0m"
    DRONE_COLOR = "\033[38;5;226m"  # bright yellow for drones

    @staticmethod
    def _get_color(color_name: str | None) -> str:
        if color_name is None:
            return Simulator.DEFAULT_COLOR
        return Simulator.ANSI_COLORS.get(
            color_name.lower(), Simulator.DEFAULT_COLOR
        )

    def get_zone_by_name(self, zone_name: str) -> Union[Zone, None]:
        for zone in self.zones:
            if zone.name == zone_name:
                return zone
        return None

    def _colored(self, name: str) -> str:
        RESET: str = Simulator.RESET
        colored_str: str = ""
        if "-" in name:
            zone1, zone2 = name.split("-")
            zone1_obj1 = self.get_zone_by_name(zone1)
            zone1_obj2 = self.get_zone_by_name(zone2)
            if zone1_obj1 is None or zone1_obj2 is None:
                return self.DEFAULT_COLOR
            color_name1 = zone1_obj1.color
            color_name2 = zone1_obj2.color
            color1 = self._get_color(color_name1)
            color2 = self._get_color(color_name2)
            colored_str = (
                f"{color1}{zone1}{RESET}"
                f"{'-'}"
                f"{color2}{zone2}{RESET}"
            )
        else:
            zone_obj = self.get_zone_by_name(name)
            if zone_obj is None:
                return self.DEFAULT_COLOR
            color_name = zone_obj.color
            color = self._get_color(color_name)
            colored_str = (f"{color}{name}{RESET}")
        return colored_str

    def create_drones(self) -> None:
        for i in range(self.nb_drones):
            drone = Drone(
                drone_id=f"D{i+1}",
                assigned_path=[],
                current_location=self.start
            )
            self.drones.append(drone)

    def assign_drones_to_paths(self) -> List[Drone]:
        if not self.paths:
            raise ValueError("No valid paths found.")
        unique_paths = min(len(self.drones), len(self.paths))
        for i, drone in enumerate(self.drones):
            path_idx = i % unique_paths
            drone.assigned_path = self.paths[path_idx]
            drone.current_location = drone.assigned_path[0]
            self.start.current_drones.append(drone)
        return self.drones

    def get_next_zone(self, drone: Drone) -> Optional[Zone]:
        next_idx = drone.path_index + 1
        if next_idx >= len(drone.assigned_path):
            return None
        return drone.assigned_path[next_idx]

    def find_connection(self, zone: Zone, dest: Zone) -> Optional[Connection]:
        for conn in self.conns:
            if (
                conn.zone1 == zone.name and conn.zone2 == dest.name
            ) or (
                conn.zone2 == zone.name and conn.zone1 == dest.name
            ):
                return conn
        return None

    def can_drone_move(self, drone: Drone) -> bool:
        if drone.is_delivered:
            return False
        next_zone = self.get_next_zone(drone)

        if next_zone is None:
            return False
        conn = self.find_connection(
            drone.current_location,
            next_zone
        )

        if conn is None:
            return False
        if len(conn.current_drones) >= conn.max_link_capacity:
            return False

        future_occupancy = len(next_zone.current_drones)
        for d in self.drones:
            if d.target_zone == next_zone:
                future_occupancy += 1
        if next_zone is not self.end:
            if future_occupancy >= next_zone.max_drones:
                return False

        return True

    def move_normal_drone(self, drone: Drone, next_zone: Zone) -> None:
        zone = drone.current_location
        zone.current_drones.remove(drone)
        next_zone.current_drones.append(drone)
        drone.current_location = next_zone
        drone.path_index += 1

        if next_zone == self.end:
            drone.is_delivered = True

    def move_restricted_drone(self, drone: Drone) -> None:
        zone = drone.current_location
        next_zone = self.get_next_zone(drone)
        if next_zone is None:
            return
        conn = self.find_connection(zone, next_zone)

        if not conn:
            return

        zone.current_drones.remove(drone)
        conn.current_drones.append(drone)
        drone.current_connection = conn
        drone.target_zone = next_zone
        drone.turns_left = 1

    def update_transit_drones(self) -> List[Drone]:
        arrived = []

        for drone in self.drones:
            if not drone.current_connection:
                continue

            drone.turns_left -= 1

            if drone.turns_left > 0:
                continue

            conn = drone.current_connection
            target = drone.target_zone
            if target is None:
                continue

            if drone in conn.current_drones:
                conn.current_drones.remove(drone)

            target.current_drones.append(drone)
            drone.current_location = target
            drone.path_index += 1
            drone.current_connection = None
            drone.target_zone = None
            drone.turns_left = 0

            if target is self.end:
                drone.is_delivered = True

            arrived.append(drone)

        return arrived

    def run(self) -> None:
        while not all(d.is_delivered for d in self.drones):

            turn_moves = []

            arrived = self.update_transit_drones()

            for drone in self.drones:

                if drone.is_delivered:
                    continue

                # Drone has just arrived this turn.
                if drone in arrived:
                    turn_moves.append(
                        f"{drone.drone_id}: "
                        f"{self._colored(drone.current_location.name)}"
                    )
                    continue

                # Already crossing a restricted connection.
                if drone.current_connection:
                    continue

                if not self.can_drone_move(drone):
                    continue

                next_zone = self.get_next_zone(drone)
                if next_zone is None:
                    continue
                if next_zone.zone_type == ZoneType.RESTRICTED:
                    self.move_restricted_drone(drone)
                    conn = drone.current_connection
                    if conn is None:
                        continue
                    move = (
                        f"{drone.drone_id}: "
                        f"{self._colored(conn.name)}"
                    )

                else:
                    self.move_normal_drone(drone, next_zone)
                    move = (
                        f"{drone.drone_id}: "
                        f"{self._colored(next_zone.name)}"
                    )

                turn_moves.append(move)

            # Build frame every turn
            frame: Dict[str, Union[Zone, Connection]] = {}

            for drone in self.drones:
                current_connection = drone.current_connection
                if current_connection is not None:
                    frame[drone.drone_id] = current_connection
                else:
                    frame[drone.drone_id] = drone.current_location

            self.frames.append(frame)
            self.turn_logs.append(" ".join(turn_moves))

    def get_output(self) -> None:
        print("turns: ", len(self.turn_logs), end="\n\n")
        for i, log in enumerate(self.turn_logs, start=1):
            print(f"Turn {i}: ", (log))
