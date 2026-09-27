import pygame
from pygame.sprite import Sprite
from typing import Optional


class Bullet(Sprite):
    """A class to manage bullet fired from the ship"""

    def __init__(self, root):

        super().__init__()

        self.main_screen = root.screen
        self.settings = root.settings
        self.b_color = self.settings.bullet_color

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )

        self.rect.midtop = root.ship.rect.midtop

        self.y: Optional[float | int] = float(self.rect.y)

    def draw_bullet(self):

        pygame.draw.rect(self.main_screen, self.b_color, self.rect)

    def update(self):

        self.y -= self.settings.bullet_speed

        self.rect.y = self.y
