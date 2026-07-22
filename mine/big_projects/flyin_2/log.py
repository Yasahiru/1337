
class Test:

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
            if d == drone:
                break

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
