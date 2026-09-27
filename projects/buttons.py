import pygame

from projects.settings import settings


class Buttons:

    def __init__(self, screen):

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.play_rect = pygame.Rect(
            0, 0, settings.button_width, settings.button_height
        )

        self.exit_rect = pygame.Rect(
            0, 0, settings.button_width, settings.button_height
        )

        self.play_rect.center = self.screen_rect.center
        self.play_rect.top = settings.screen_height / 2 - 30

        self.exit_rect.center = self.screen_rect.center
        self.exit_rect.top = settings.screen_height / 2 + 30

        self.font = pygame.font.SysFont("consolas", 20)

        self.prep_text()

    def prep_text(self):

        self.play_image = self.font.render("Play", True, "#FFF3D5")
        self.play_image_rect = self.play_image.get_rect()
        self.play_image_rect.center = self.play_rect.center

        self.exit_image = self.font.render("Exit", True, "#FFF3D5")
        self.exit_image_rect = self.exit_image.get_rect()
        self.exit_image_rect.center = self.exit_rect.center

    def draw(self):

        pygame.draw.rect(self.screen, settings.button_color, self.play_rect)
        pygame.draw.rect(self.screen, settings.button_color, self.exit_rect)

        self.screen.blit(self.play_image, self.play_image_rect)
        self.screen.blit(self.exit_image, self.exit_image_rect)
