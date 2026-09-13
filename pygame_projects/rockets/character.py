import pygame


class Character:
    def __init__(self, root):

        self.main_screen = root.screen

        self.settings = root.settings

        self.main_screen_rect = self.main_screen.get_rect()

        # load character image
        self.char_img = pygame.image.load("images/ship.bmp")
        self.char_img_rect = self.char_img.get_rect()
        self.char_img_rect.center = self.main_screen_rect.center

        self.x = float(self.char_img_rect.x)
        self.y = float(self.char_img_rect.y)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):

        self.main_screen.blit(self.char_img, self.char_img_rect)

    def update(self):
        if self.moving_left and self.char_img_rect.left > self.main_screen_rect.left:
            self.x -= self.settings.char_speed
        elif (
            self.moving_right and self.char_img_rect.right < self.main_screen_rect.right
        ):
            self.x += self.settings.char_speed
        elif self.moving_up and self.char_img_rect.top > self.main_screen_rect.top:
            self.y -= self.settings.char_speed
        elif (
            self.moving_down
            and self.char_img_rect.bottom < self.main_screen_rect.bottom
        ):
            self.y += self.settings.char_speed

        self.char_img_rect.x = self.x
        self.char_img_rect.y = self.y
