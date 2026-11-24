import pygame


class AudioManager:
    @classmethod
    def pre_init(cls):
        # Fix sound lag
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)

    def __init__(
        self, bg_volume: float = 1.0, sfx_volume: float = 0.5, mute: bool = False
    ) -> None:
        self.bg_volume = bg_volume
        self.sfx_volume = sfx_volume
        self.mute = mute
        # SFXs
        self.sfxs: list[pygame.mixer.Sound] = []

    def toggle_mute(self) -> None:
        self.mute = not self.mute

    def check_mute(self) -> None:
        if self.mute:
            pygame.mixer.music.set_volume(0)
            [sfx.set_volume(0) for sfx in self.sfxs]
        else:
            pygame.mixer.music.set_volume(self.bg_volume)
            [sfx.set_volume(self.sfx_volume) for sfx in self.sfxs]
