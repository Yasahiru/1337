import pygame
from visualization.color import get_color


class Visualizer:

    def __init__(self, zones, conns):
        pygame.init()
        pygame.display.set_caption("Flyin Simulation")

        self.zones = zones
        self.conns = conns

        self.width = 1400
        self.height = 800
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )

    def run(self):
        BACKGROUND = (240, 240, 240)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(BACKGROUND)

            for zone in self.zones:
                x = zone.x
                y = zone.y
                color = get_color(zone.color)

                pygame.draw.circle(
                    self.screen,
                    color,
                    (x, y),
                    100,
                )

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
