from model.drone import Drone
from model.zone import Zone
from model.zone_type import ZoneType
from typing import Optional, List
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
        self.turn_logs = []
        self.frames = []

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

    def get_zone_by_name(self, zone_name: str) -> Zone:
        for zone in self.zones:
            if zone.name == zone_name:
                return zone
        return None

    def _colored(self, name: str) -> str:
        RESET: str = Simulator.RESET
        colored_str: str = ""
        if "-" in name:
            zone1, zone2 = name.split("-")
            color_name1 = self.get_zone_by_name(zone1).color
            color_name2 = self.get_zone_by_name(zone2).color
            color1 = self._get_color(color_name1)
            color2 = self._get_color(color_name2)
            colored_str = (
                f"{color1}{zone1}{RESET}"
                f"{'-'}"
                f"{color2}{zone2}{RESET}"
            )
        else:
            color_name = self.get_zone_by_name(name).color
            color = self._get_color(color_name)
            colored_str = (f"{color}{name}{RESET}")

        return colored_str

    def create_drones(self) -> None:
        # print("create drones")
        for i in range(self.nb_drones):
            drone = Drone(
                drone_id=f"D{i+1}",
                assigned_path=[],
                current_location=self.start
            )
            self.drones.append(drone)

    def assign_drones_to_paths(self) -> List[Drone]:
        # print("assign_drones_to_paths")
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
        # print("get_next_zone")
        next_idx = drone.path_index + 1
        if next_idx >= len(drone.assigned_path):
            return None
        return drone.assigned_path[next_idx]

    def find_connection(self, zone: Zone, dest: Zone) -> Optional[Connection]:
        # print("\n find_connection")
        for conn in self.conns:
            if conn.zone1 == zone.name:
                if conn.zone2 == dest.name:
                    return conn
            elif conn.zone2 == zone.name:
                if conn.zone1 == dest.name:
                    return conn
        return None

    def can_drone_move(self, drone: Drone) -> bool:
        # print("can_drone_move")
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

        return True

    def move_normal_drone(self, drone: Drone, next_zone: Zone) -> None:
        # print("\nmove_normal_drone")

        zone = drone.current_location
        zone.current_drones.remove(drone)
        if next_zone is None:
            return

        next_zone.current_drones.append(drone)
        drone.current_location = next_zone

        # increment the path index
        drone.path_index += 1

        # check if the drone has arrived
        if next_zone == self.end:
            drone.is_delivered = True

    def move_restricted_drone(self, drone: Drone) -> None:
        # print("move_restricted_drone")
        zone = drone.current_location
        zone.current_drones.remove(drone)

        next_zone = self.get_next_zone(drone)
        conn = self.find_connection(zone=zone, dest=next_zone)

        if not conn:
            return

        conn.current_drones.append(drone)
        drone.target_zone = next_zone
        drone.current_connection = conn
        drone.turns_left = 2

    def update_transit_drones(self) -> None:
        # print("\nupdate_transit_drones")

        for d in self.drones:
            if not d.current_connection:
                continue

            d.turns_left -= 1
            if d.turns_left > 0:
                continue

            target = d.target_zone
            conn = d.current_connection

            if d in conn.current_drones:
                conn.current_drones.remove(d)

            if len(target.current_drones) >= target.max_drones:
                continue

            target.current_drones.append(d)
            d.current_location = target
            d.path_index += 1

            d.target_zone = None
            d.current_connection = None
            d.turns_left = 0

            if target == self.end:
                d.is_delivered = True
                continue

    def run(self) -> None:
        while not all(d.is_delivered for d in self.drones):
            turn_moves = []
            frame = {}

            self.update_transit_drones()

            for drone in self.drones:
                if drone.is_delivered:
                    continue
                if drone.current_connection:
                    continue
                if not self.can_drone_move(drone):
                    continue

                move = None
                next_zone = self.get_next_zone(drone)
                if next_zone.zone_type == ZoneType.RESTRICTED:
                    self.move_restricted_drone(drone)
                    conn = self.find_connection(
                        drone.current_location,
                        next_zone
                    )
                    move = f"{drone.drone_id}: {self._colored(conn.name)}"
                    frame[drone.drone_id] = conn.name
                else:
                    move = f"{drone.drone_id}: {self._colored(next_zone.name)}"
                    self.move_normal_drone(drone, next_zone)
                    frame[drone.drone_id] = next_zone.name

                if move:
                    turn_moves.append(move)

            if len(turn_moves) > 0:
                self.turn_logs.append(" ".join(turn_moves))
                self.frames.append(frame)

    def get_output(self) -> None:
        print("turns: ", len(self.turn_logs), end="\n\n")
        for i, log in enumerate(self.turn_logs, start=1):
            print(f"Turn {i}: ", (log))
