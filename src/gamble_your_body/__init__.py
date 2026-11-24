import pygame

from .player_monkey import PlayerMonkey

# TODO
# - [ ] BG img
# - [ ] P1 & P2 assets: player-img, bullet-img, damage-img


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

        # Settings
        self.players_velocity = 400

        # Players
        self.player_1 = PlayerMonkey(self.win, 500, 600, 64, 64, self.players_velocity)

    def run(self) -> None:
        self.running = True

        while self.running:
            # FPS and Delta
            self.delta = self.clock.tick(self.fps) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()

            # P1 controls
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player_1.go_left(self.delta)
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player_1.go_right(self.delta)

            self.player_1.is_walking = (
                keys[pygame.K_LEFT]
                or keys[pygame.K_RIGHT]
                or keys[pygame.K_a]
                or keys[pygame.K_d]
            )

            self.paint()

        pygame.quit()

    def paint(self) -> None:
        # Repainting the window means erasing past positioned drawings
        self.win.fill((0, 0, 0))

        # Players
        self.player_1.draw(self.delta)

        # Update display
        pygame.display.update()


def main() -> None:
    game = Game()
    game.run()
