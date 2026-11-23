import pygame


class Game:
    def __init__(self) -> None:
        # Ratio 16:9
        self.width = 1280
        self.height = 720
        self.fps = 60
        self.running = False

        pygame.init()
        pygame.display.set_caption("Gamble Your Body")
        self.win = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        self.running = True

        while self.running:
            # FPS and Delta
            self.delta = self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.paint()

        pygame.quit()

    def paint(self) -> None:
        # Repainting the window means erasing past positioned drawings
        self.win.fill((0, 0, 0))

        # Update display
        pygame.display.update()


def main() -> None:
    game = Game()
    game.run()
