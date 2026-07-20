import pygame
from color import get_color
from connection import Connection
from zone_model import Zone
from typing import Dict, List, Union
import sys


class Visualizer:

    WINDOW_WIDTH = 1800
    WINDOW_HEIGHT = 900
    BACKGROUND = (210, 210, 210)
    ZONE_RADIUS = 30
    CONNECTION_WIDTH = 4
    MARGIN = 40
    FRAME_TIME = 1000

    def __init__(
        self,
        zones: List[Zone],
        conns: List[Connection],
        frames: List[Dict[str, Union[Zone, Connection]]],
    ) -> None:
        pygame.init()
        pygame.display.set_caption("Flyin Simulation")

        _mode = (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.screen = pygame.display.set_mode(_mode)

        self.zones: List[Zone] = zones
        self.conns = conns
        self.frames = frames
        self.zone_coords: Dict[str, tuple[int, int]] = {}
        self.compute_camera()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 22)
        self.current_frame = 0

    def get_zone_by_name(self, zone_name: str) -> Union[Zone, None]:
        for zone in self.zones:
            if zone.name == zone_name:
                return zone
        return None

    def compute_camera(self) -> None:
        self.min_x = min(z.x for z in self.zones)
        self.max_x = max(z.x for z in self.zones)
        self.min_y = min(z.y for z in self.zones)
        self.max_y = max(z.y for z in self.zones)

        usable_width = self.WINDOW_WIDTH - 2 * self.MARGIN
        usable_height = self.WINDOW_HEIGHT - 2 * self.MARGIN
        scale_x = usable_width / max(1, self.max_x - self.min_x)
        scale_y = usable_height / max(1, self.max_y - self.min_y)

        self.scale = min(scale_x, scale_y)

        map_width = (self.max_x - self.min_x) * self.scale
        map_height = (self.max_y - self.min_y) * self.scale

        self.offset_x = (self.WINDOW_WIDTH - map_width) / 2
        self.offset_y = (self.WINDOW_HEIGHT - map_height) / 2

    def world_to_screen(self, x: int, y: int) -> tuple[int, int]:
        _compute = (x - self.min_x) * self.scale + self.offset_x
        screen_x = int(_compute)
        _compute = (y - self.min_y) * self.scale + self.offset_y
        screen_y = int(_compute)

        return screen_x, screen_y

    def draw_connections(self) -> None:
        for conn in self.conns:
            zone1 = self.get_zone_by_name(conn.zone1)
            zone2 = self.get_zone_by_name(conn.zone2)

            if zone1 is None or zone2 is None:
                continue

            x1, y1 = self.world_to_screen(zone1.x, zone1.y)
            x2, y2 = self.world_to_screen(zone2.x, zone2.y)
            pygame.draw.line(
                self.screen,
                (60, 60, 60),
                (x1, y1),
                (x2, y2),
                self.CONNECTION_WIDTH,
            )

    def draw_zones(self) -> None:
        for zone in self.zones:
            x, y = self.world_to_screen(zone.x, zone.y)
            self.zone_coords[zone.name] = (x, y)

            pygame.draw.circle(
                self.screen,
                get_color(zone.color),
                (x, y),
                self.ZONE_RADIUS,
            )
            pygame.draw.circle(
                self.screen,
                (0, 0, 0),
                (x, y),
                self.ZONE_RADIUS,
                2,
            )

    def draw_labels(self) -> None:
        for zone in self.zones:
            x, y = self.world_to_screen(zone.x, zone.y)
            drones = len(zone.current_drones)
            label = self.font.render(
                str(drones),
                True,
                (0, 0, 0),
            )
            rect = label.get_rect(center=(x, y))
            self.screen.blit(label, rect)

    def draw_drone(
        self,
        frame: Dict[str, Union[Zone, Connection]],
    ) -> None:
        DRONE_RADIUS = 10

        for drone_id, location in frame.items():
            if isinstance(location, Zone):
                x, y = self.zone_coords[location.name]
            else:
                x1, y1 = self.zone_coords[location.zone1]
                x2, y2 = self.zone_coords[location.zone2]

                x = (x1 + x2) // 2
                y = (y1 + y2) // 2

            pygame.draw.circle(
                self.screen,
                (255, 255, 255),
                (x, y),
                DRONE_RADIUS,
            )

            pygame.draw.circle(
                self.screen,
                (0, 0, 0),
                (x, y),
                DRONE_RADIUS,
                2,
            )

            label = self.font.render(
                drone_id,
                True,
                (0, 0, 0),
            )

            self.screen.blit(
                label,
                (x + 12, y - 8),
            )

    def run(self) -> None:

        try:
            frame_index = 0
            last_update = pygame.time.get_ticks()

            running = True

            while running:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                now = pygame.time.get_ticks()

                if (
                    now - last_update >= self.FRAME_TIME
                    and frame_index < len(self.frames) - 1
                ):
                    frame_index += 1
                    last_update = now

                self.screen.fill(self.BACKGROUND)
                self.draw_connections()
                self.draw_zones()

                if self.frames:
                    self.draw_drone(self.frames[frame_index])

                pygame.display.flip()
                self.clock.tick(60)

            pygame.quit()
        except KeyboardInterrupt:
            sys.exit
