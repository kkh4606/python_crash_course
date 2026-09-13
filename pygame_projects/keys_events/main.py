import pygame
import sys


class Test(pygame.sprite.Sprite):
    def __init__(self, root):
        super().__init__()

        self.screen = root.screen()

        # loag image
        self.image = pygame.image.load("images/")


class KeyEvent:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((1280, 720))

    def run(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    print(f"You clicked '{event.key}' key")


if __name__ == "__main__":
    key = KeyEvent()
    key.run()
