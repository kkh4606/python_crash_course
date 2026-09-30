import pygame

from projects.settings import settings


class Board:

    def __init__(self, screen):

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, settings.board_width, settings.board_height)

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = self.rect.x

        self.moving_left = False
        self.moving_right = False

    def draw(self):

        pygame.draw.rect(self.screen, settings.board_color, self.rect)

    def move(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += settings.board_speed

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= settings.board_speed

        self.rect.x = self.x

    def reset_board_position(self):

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = self.rect.x

        ...
