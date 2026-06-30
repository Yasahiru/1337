import pygame
from visualization.color import get_color
from model.zone import Zone


class Visualizer:

    WINDOW_WIDTH = 1800
    WINDOW_HEIGHT = 900
    BACKGROUND = (210, 210, 210)
    ZONE_RADIUS = 30
    CONNECTION_WIDTH = 4
    MARGIN = 40

    def __init__(self, zones, conns, frames):
        pygame.init()
        pygame.display.set_caption("Flyin Simulation")

        self.screen = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        )

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 22)
        self.zones = zones
        self.conns = conns
        self.frames = frames
        self.current_frame = 0
        self.compute_camera()

    def get_zone_by_name(self, zone_name: str) -> Zone:
        for zone in self.zones:
            if zone.name == zone_name:
                return zone
        return None

    def compute_camera(self):
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

    def world_to_screen(self, x, y):
        screen_x = int(
            (x - self.min_x) * self.scale + self.offset_x
        )
        screen_y = int(
            (y - self.min_y) * self.scale + self.offset_y
        )

        return screen_x, screen_y

    def draw_connections(self):
        for conn in self.conns:
            zone1 = self.get_zone_by_name(conn.zone1)
            zone2 = self.get_zone_by_name(conn.zone2)

            x1, y1 = self.world_to_screen(
                zone1.x,
                zone1.y
            )
            x2, y2 = self.world_to_screen(
                zone2.x,
                zone2.y
            )
            pygame.draw.line(
                self.screen,
                (60, 60, 60),
                (x1, y1),
                (x2, y2),
                self.CONNECTION_WIDTH,
            )

    def draw_zones(self):
        for zone in self.zones:
            x, y = self.world_to_screen(zone.x, zone.y)
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

    def draw_labels(self):
        for zone in self.zones:
            x, y = self.world_to_screen(zone.x, zone.y)
            label = self.font.render(
                zone.name,
                True,
                (0, 0, 0),
            )
            rect = label.get_rect(
                center=(x, y - 45)
            )
            self.screen.blit(label, rect)

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.BACKGROUND)
            self.draw_connections()
            self.draw_zones()
            self.draw_labels()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
