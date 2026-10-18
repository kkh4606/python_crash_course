import random

import pygame

from projects.board import Board
from projects.ball import Ball
from projects.buttons import Buttons
from projects.scoreboard import Scoreboard
from projects.settings import settings
from projects.target import Target

COLORS = ["#ffe295", "#3a7d9c", "#9c8ca0", "#700fbe"]


class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height)
        )

        self.screen_rect = self.screen.get_rect()

        self.running = True
        self.clock = pygame.time.Clock()

        self.targets = pygame.sprite.Group()
        self.scoreboard = Scoreboard(self.screen)
        self.ball = Ball(self.screen)
        self.board = Board(self.screen)
        self.buttons = Buttons(self.screen)

        self.game_active = False

        self.create_target_objects()

        for target in self.targets.sprites():

            target.color = random.choice(COLORS)

    def run(self):

        while self.running:

            self.check_events()

            self.display_screen()
            self.clock.tick(settings.fps)

    def create_target_objects(self):

        target = Target(self.screen)

        width, height = target.rect.size

        current_x, current_y = 0, 0

        while current_y < settings.screen_height - 400:

            while current_x < settings.screen_width:

                new_target = Target(self.screen)

                new_target.rect.x = current_x

                new_target.rect.y = current_y

                self.targets.add(new_target)

                current_x += width + 5

            current_y += width + 5

            current_x = 0

    def update_screen(self):

        self.check_collisions()
        self.ball.update()

        self.board.move()

    def display_screen(self):

        self.screen.fill(settings.bg_color)

        # render
        for target in self.targets.sprites():
            target.draw_target()
        self.scoreboard.show_score_level()

        self.board.draw()
        self.ball.draw_ball()

        if self.game_active:

            self.update_screen()

        if not self.game_active:
            self.buttons.draw()

        pygame.display.flip()

    def click_play_button(self, pos):

        clicked = self.buttons.play_rect.collidepoint(pos)

        if clicked:

            self.game_active = True

            self.board.reset_board_position()

            self.ball.reset_ball_position()

    def check_collisions(self):

        if self.ball.rect.top <= 0 or self.ball.rect.bottom >= settings.screen_height:

            settings.ball_speed_y *= -1

        if self.ball.rect.left < 0 or self.ball.rect.right > settings.screen_width:

            settings.ball_speed_x *= -1

        if self.ball.rect.colliderect(self.board.rect):
            settings.ball_speed_y *= -1

        for target in self.targets.sprites():

            if self.ball.rect.colliderect(target.rect):
                settings.ball_speed_y *= -1
                self.targets.remove(target)

    def check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                self.check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self.check_key_release_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.click_play_button(mouse_pos)

                if self.buttons.exit_rect.collidepoint(mouse_pos):
                    self.running = False

    def check_key_down_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.board.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.board.moving_left = True

        elif event.key == pygame.K_p:
            self.game_active = True

    def check_key_release_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.board.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.board.moving_left = False


if __name__ == "__main__":
    g = Game()
    g.run()
