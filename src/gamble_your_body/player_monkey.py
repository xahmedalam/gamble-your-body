import pygame

from .utils import create_sprite_sheet


class PlayerMonkey:
    def __init__(
        self,
        win: pygame.Surface,
        x: float,
        y: float,
        width: int,
        height: int,
        velocity: int,
    ) -> None:
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.sprite_size = (32, 32)
        self.sprite_scale_size = (self.width, self.height)

        # Sprite idle
        self.sprite_idle_strip_count = 5
        self.sprite_idle = create_sprite_sheet(
            "src/assets/img/monkey-idle-strip5.png",
            self.sprite_idle_strip_count,
            self.sprite_size,
            self.sprite_scale_size,
            True,
        )

        # Sprite walk
        self.sprite_walk_strip_count = 6
        self.sprite_walk = create_sprite_sheet(
            "src/assets/img/monkey-walk-strip6.png",
            self.sprite_walk_strip_count,
            self.sprite_size,
            self.sprite_scale_size,
        )

        # Collision
        self.collision = pygame.Rect((self.x, self.y, self.width, self.height))

    def draw(self, delta: float) -> None:
        # Draw sprite
        self.win.blit(self.sprite_idle[0], (self.x, self.y))

        # Update collision
        self.collision.topleft = (self.x, self.y)

    def go_left(self, delta: float) -> None:
        self.x -= self.velocity * delta
        self.clamping()

    def go_right(self, delta: float) -> None:
        self.x += self.velocity * delta
        self.clamping()

    def clamping(self) -> None:
        self.x = min(self.x, self.win.width - self.width)
        self.x = max(self.x, 0)
