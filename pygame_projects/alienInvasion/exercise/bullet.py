import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, root):
        super().__init__()
        self.main_screen = root.screen

        self.settings = root.settings

        self.bullet_color = self.settings.bullet_color

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_height, self.settings.bullet_width
        )

        self.rect.midright = root.ship.play_rect.midright

        self.x = self.rect.x

    def draw_bullet(self):

        pygame.draw.rect(self.main_screen, self.bullet_color, self.rect)

    def update(self):

        self.x += self.settings.bullet_speed

        self.rect.x = self.x
