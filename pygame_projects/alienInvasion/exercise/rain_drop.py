import sys
import pygame

from pygame_projects.alienInvasion.bullet import Bullet
from pygame_projects.alienInvasion.settings import Settings
from pygame_projects.alienInvasion.ship import Ship
from pygame_projects.alienInvasion.alien import Alien


class AlienInvasion:

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row"""
        new_alien = Alien(self)

        new_alien.y = y_position
        new_alien.rect.x = x_position

        new_alien.rect.y = y_position

        self.aliens.add(new_alien)

    def _check_fleet_edge(self):

        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Create the fleet of aliens."""

        # Make an alien

        alien = Alien(self)

        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)

                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # self.bullets.update()
        self._update_bullets()
        self._update_aliens()
        self.aliens.draw(self.screen)

        self.ship.blitme()

        pygame.display.flip()

    def _update_aliens(self):
        self._check_fleet_edge()
        self.aliens.update()
        ...

    def _update_bullets(self):
        """Update position of bullets and delete old bullets"""
        # Update bullets position
        self.bullets.update()

        # Get rid of old bullets that have disappeared
        for bullet in self.bullets.sprites():
            if bullet.b_rect.bottom < 0:
                print(f"bullet pos has reached 0")
                self.bullets.remove(bullet)
            bullet.draw_bullet()

    def _fire_bullet(self):

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
