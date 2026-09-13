import sys
import random
import pygame


class Star(pygame.sprite.Sprite):

    def __init__(self, root):
        super().__init__()

        self.screen = root.screen

        # load the image

        self.image = pygame.image.load("images/star.bmp")

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))

        self.stars = pygame.sprite.Group()

        self._fleet_stars()

    def _make_star(self, x_pos, y_pos):

        pos = []
        r_x = None
        r_y = None

        while r_x not in pos and r_y not in pos:

            r_x = random.randint(x_pos, 1152)
            r_y = random.randint(y_pos, 464)

            pos.extend([r_x, r_y])

        new_star = Star(self)
        new_star.rect.x = r_x
        new_star.rect.y = r_y
        self.stars.add(new_star)

    def _fleet_stars(self):

        star = Star(self)
        star_width, star_height = star.rect.size
        current_x, current_y = star_width, star_height

        while current_y < 720 - (4 * star_width):

            while current_x < 1280 - (2 * star_width):

                self._make_star(current_x, current_y)

                current_x += star_width * 2

            current_y += star_width * 2
            current_x = star_width

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill("white")

            self.stars.draw(self.screen)

            pygame.display.flip()


g = Game()
g.run()
