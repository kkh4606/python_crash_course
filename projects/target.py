import pygame


class Target(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        self.rect = pygame.Rect(0, 0, 20, 20)

        self.x = self.rect.x

        self.y = self.rect.y

        self.color = None

    def draw_target(self):

        pygame.draw.rect(self.screen, self.color, self.rect)
