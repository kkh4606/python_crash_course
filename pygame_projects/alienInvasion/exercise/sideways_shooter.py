import random
import sys

import pygame

from pygame_projects.alienInvasion.exercise.bullet import Bullet
from pygame_projects.alienInvasion.settings import Settings
from pygame_projects.alienInvasion.exercise.ship import Ship


class Alien(pygame.sprite.Sprite):
    def __init__(self, root):
        super().__init__()

        self.screen = root.screen

        self.screen_rect = self.screen.get_rect()

        self.settings = root.settings

        # load image

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = 900

        self.y = 0

        self.x = float(self.rect.x)

    def update(self, *args, **kwargs):

        self.y -= self.settings.alien_speed * self.settings.fleet_direction

        self.rect.y = self.y

    def check_edges(self):

        return (self.rect.top <= 0) or (self.rect.bottom >= self.screen_rect.bottom)

    def move_left(self):

        self.x -= self.settings.fleet_drop_speed

        self.rect.x = self.x


class SidewayShooter:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.screen_rect = self.screen.get_rect()

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        pygame.display.set_caption("Sideways Shooter")

        self._create_alien_fleet()

    def _create_alien(self, current_x, current_y):

        new_alien = Alien(self)

        width = new_alien.rect.width
        new_alien.rect.x = current_x - width
        new_alien.rect.y = current_y
        new_alien.x = new_alien.rect.x
        new_alien.y = new_alien.rect.y

        self.aliens.add(new_alien)

    def _create_alien_fleet(self):

        alien = Alien(self)

        height, width = alien.rect.size
        padding = 10

        maximum_bottom = self.screen_rect.height - (2 * height)

        maximum_left = self.screen_rect.width - (5 * width)

        current_x, current_y = alien.x, alien.rect.height

        # print(current_x, current_y, maximum_left, maximum_bottom, end="  ")

        while current_y < maximum_bottom:

            while current_x > maximum_left:

                self._create_alien(current_x, current_y)

                current_x -= alien.rect.width + padding

            current_y += height + padding
            current_x = alien.x

    def _check_fleet_edges(self):

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):

        for alien in self.aliens.sprites():
            alien.move_left()

        self.settings.fleet_direction *= -1

    def run(self):

        while True:

            self._check_events()

            self.ship.update()

            self._update_screen()

            self.clock.tick(60)

    def _update_screen(self):

        self.screen.fill(self.settings.bg_color)
        self._update_bullet()
        self.ship.blit_ship()
        self._update_aliens()

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._key_pressed(event)

            elif event.type == pygame.KEYUP:
                self._key_released(event)

    def _key_pressed(self, event):

        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _key_released(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_aliens(self):

        pygame.sprite.groupcollide(self.aliens, self.bullets, True, False)

        if len(self.aliens) == 0:
            self._create_alien_fleet()
        self._check_fleet_edges()
        self.aliens.update()

        self.aliens.draw(self.screen)

    def _update_bullet(self):

        self.bullets.update()

        for bullet in self.bullets.sprites():

            # remove old bullets disappeared

            if bullet.rect.right > self.screen.get_rect().right:
                self.bullets.remove(bullet)
            bullet.draw_bullet()


if __name__ == "__main__":
    game = SidewayShooter()
    game.run()
