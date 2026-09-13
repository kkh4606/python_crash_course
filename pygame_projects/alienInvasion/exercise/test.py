import sys

import pygame
from pygame.sprite import Sprite


class Test:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Test")

    def run(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("you click mouse")

            self.screen.fill("white")

            pygame.display.flip()


t = Test()
t.run()
