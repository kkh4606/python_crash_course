# Example file showing a basic pygame "game loop"
import pygame
import sys


from pygame_projects.rockets.character import Character
from pygame_projects.rockets.game_settings import Settings


class Rocket:
    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.clock = pygame.time.Clock()
        self.running = True

        self.char = Character(self)

    def run_game(self):

        while self.running:
            self._check_events()
            self.char.update()
            self._update_screen()
            self.clock.tick(60)  # limits FPS to 60
        pygame.quit()

    def _check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self._key_pressed(event)

            elif event.type == pygame.KEYUP:
                self._key_released(event)

    def _key_pressed(self, event):

        if event.key == pygame.K_LEFT:
            self.char.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.char.moving_right = True
        elif event.key == pygame.K_UP:
            self.char.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.char.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()

    def _key_released(self, event):

        if event.key == pygame.K_LEFT:
            self.char.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.char.moving_right = False
        elif event.key == pygame.K_UP:
            self.char.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.char.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.char.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    r = Rocket()
    r.run_game()
