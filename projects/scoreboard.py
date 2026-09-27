import pygame.font


class Scoreboard:

    def __init__(self, screen):
        self.screen = screen

        self.font = pygame.font.SysFont("consolas", 20, False, italic=True)

        self.score = 0
        self.level = 1

        self.prep_score_and_level()

    def prep_score_and_level(self):

        self.score_image = self.font.render(
            f"score: {self.score}", True, (255, 255, 255)
        )
        self.score_image_rect = self.score_image.get_rect()

        self.score_image_rect.x = 5
        self.score_image_rect.y = 5

        self.level_image = self.font.render(
            f"level: {self.level}", True, (255, 255, 255)
        )
        self.level_image_rect = self.level_image.get_rect()

        self.level_image_rect.x = 5
        self.level_image_rect.y = 30

    def show_score_level(self):

        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
