import pygame
from pathlib import Path

image_dir = Path().resolve().parent / "images" / "ship.bmp"


class Ship:
    """A class to manage the ship."""

    def __init__(self, root):
        """Initialize the ship and set its starting position."""
        self.screen = root.screen

        self.screen_rect = root.screen.get_rect()
        self.settings = root.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        self.y = self.rect.y
        self.moving_up = False
        self.moving_down = False

    def blit_ship(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y
