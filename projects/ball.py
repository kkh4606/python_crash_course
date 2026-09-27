import pygame

from projects.board import Board
from projects.settings import settings


class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 2, settings.ball_width, settings.ball_height)
        self.rect.midtop = self.screen_rect.midtop

        self.board = Board(screen)

        self.y = self.rect.y
        self.x = self.rect.x

    def draw_ball(self):

        pygame.draw.ellipse(self.screen, settings.ball_color, self.rect)

    def update(self):

        self.rect.x += settings.ball_speed_x
        self.rect.y += settings.ball_speed_y
