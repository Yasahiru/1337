import pygame


class Visualizer:

    def __init__(self, zones, conns):
        pygame.init()
        pygame.display.set_caption("Flyin Simulation")

        self.zones = zones
        self.conns = conns

        self.width = 2200
        self.height = 1200
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

            # zones = [
            #     [(255, 0, 0), (150, 350)],
            #     [(0, 255, 0), (360, 350)],
            #     [(0, 0, 255), (580, 350)],
            #     [(0, 56, 0), (900, 350)]
            # ]

            x = 100
            for zone in self.zones:
                x *= 2
                pygame.draw.circle(
                    self.screen,
                    (255, 0, 0),
                    (zone.x + x, zone.y + x),
                    100
                )

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
