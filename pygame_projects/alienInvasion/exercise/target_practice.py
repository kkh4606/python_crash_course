import time

import pygame


class Settings:

    def __init__(self):

        # screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # rect settings
        self.width = 40
        self.height = 40
        self.color = (0, 0, 0)

        # bullets settings
        self.bullet_width = 5
        self.bullet_height = 2
        self.bullet_color = "black"

        # button settings
        self.button_width = 150
        self.button_height = 40
        self.button_color = "green"
        self.button_text_color = "white"
        self.bullet_allowed = 10

        self.speedup_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        self.ship_speed = 3
        self.bullet_speed = 10
        self.rect_speed = 2

        # 1 represent up and -1 represents down
        self.rect_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.rect_speed *= self.speedup_scale


class ResetStats:

    def __init__(self, parent):

        self.settings = parent.settings

        self.reset_stats()

    def reset_stats(self):

        self.bullet_left = self.settings.bullet_allowed


class LevelUp:
    def __init__(self):
        self.level = 1

    def level_up(self):
        self.level += 1


class LevelButton:
    def __init__(self, parent):
        self.screen = parent.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = parent.settings

        self.rect = pygame.Rect(
            0, 0, self.settings.button_width, self.settings.button_height
        )

        self.rect.x = parent.play_button.rect.x
        self.rect.y = parent.play_button.rect.y + parent.play_button.rect.height + 20

        self.prepare_msg("Level up")

    def prepare_msg(self, msg):

        font = pygame.font.Font(None, 30)

        self.msg_image = font.render(msg, True, "white")
        self.msg_image_rect = self.msg_image.get_rect()

        self.msg_image_rect.center = self.rect.center

    def draw_button(self):

        self.screen.fill("green", self.rect)

        self.screen.blit(self.msg_image, self.msg_image_rect)


class PlayButton:
    def __init__(self, parent):
        self.screen = parent.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = parent.settings
        self.font = pygame.font.Font(None, 30)

        self.rect = pygame.Rect(
            0, 0, self.settings.button_width, self.settings.button_height
        )

        self.rect.center = self.screen_rect.center

        self._prepare_text("Play")

    def _prepare_text(self, msg):
        self.msg_image = self.font.render(msg, True, self.settings.button_text_color)
        self.msg_image_rect = self.msg_image.get_rect()

        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, parent):
        super().__init__()

        self.screen = parent.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = parent.settings

        # bullet

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midleft = parent.ship.rect.midleft

        self.x, _ = self.rect.midright

    def draw_bullet(self):

        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)

    def update(self, *args, **kwargs):

        self.x -= self.settings.bullet_speed

        self.rect.right = self.x


class TargetObject:

    def __init__(self, parent):

        self.screen = parent.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = parent.settings

        self.rect = pygame.Rect(0, 10, self.settings.width, self.settings.height)

        self.y = self.rect.y

    def reset_position(self):

        self.y = 5

    def check_edge(self):
        return self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0

    def update(self):
        self.y += self.settings.rect_speed * self.settings.rect_direction

        self.rect.y = self.y

    def draw_enemy(self):
        self.screen.fill(self.settings.color, self.rect)


class Ship:

    def __init__(self, parent):

        self.screen = parent.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = parent.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.topright = self.screen_rect.topright

        self.y = self.rect.y
        self.move_up = False
        self.move_down = False

    def move(self):
        """Move the alien right or left."""
        if self.move_up and self.rect.top >= 0:

            self.y -= self.settings.ship_speed
        elif self.move_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def reset_position(self):

        self.y = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Game:

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.ship = Ship(self)
        self.enemy = TargetObject(self)
        self.bullets = pygame.sprite.Group()
        self.play_button = PlayButton(self)
        self.level_button = LevelButton(self)
        self.stats = ResetStats(self)
        self.clock = pygame.time.Clock()
        self.game_active = False
        self.running = True

        self.game_level = LevelUp()

    def run(self):

        while self.running:

            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:

            self.stats.reset_stats()
            self.game_active = True

            self.bullets.empty()
            self.enemy.reset_position()
            self.ship.reset_position()

            pygame.mouse.set_visible(False)

    def _up_game_level(self, mouse_pos):

        button_click = self.level_button.rect.collidepoint(mouse_pos)

        if button_click:

            # self.stats.reset_stats()
            # self.game_active = True
            #
            # self.bullets.empty()
            # self.enemy.reset_position()
            # self.ship.reset_position()
            #
            self.game_level.level_up()
            #
            # pygame.mouse.set_visible(False)

    def _update_enemy(self):
        self._check_rect_edge()
        self.enemy.update()

    def _check_rect_edge(self):
        if self.enemy.check_edge():

            self._change_direction()

    def _change_direction(self):

        self.settings.rect_direction *= -1

    def _show_fps(self):

        font = pygame.font.SysFont("consolas", 16)

        fps = pygame.time.Clock.get_fps(self.clock)

        fps_image = font.render(f"FPS:{fps:.2f}", True, "grey")

        self.screen.blit(fps_image, (750, 5))

    def _show_level(self):
        font = pygame.font.SysFont("consolas", 16)

        level_text = font.render(f"Level:{self.game_level.level}", True, "grey")

        self.screen.blit(level_text, (750, 20))

    def _update_screen(self):

        self.screen.fill(self.settings.bg_color)

        if self.game_active:

            self._update_enemy()

            self._update_bullets()

            self.ship.move()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemy.draw_enemy()
        self._show_fps()
        self._show_level()
        self.ship.blitme()

        if not self.game_active:
            self.level_button.draw_button()
            self.play_button.draw_button()

        pygame.display.flip()

    def _update_bullets(self):

        for bullet in self.bullets.copy():
            if bullet.x <= 0:
                self.bullets.remove(bullet)

        self.bullets.update()

        self._check_bullet_target_collisions()

    def _fire_bullets(self):

        if self.stats.bullet_left > 0:

            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

            self.stats.bullet_left -= 1

    def _check_bullet_target_collisions(self):
        if pygame.sprite.spritecollideany(self.enemy, self.bullets):

            self.game_active = False
            pygame.mouse.set_visible(True)

            self.settings.increase_speed()

        if self.stats.bullet_left == len(self.bullets) == 0:

            self.game_active = False
            pygame.mouse.set_visible(True)

            self.settings.initialize_dynamic_settings()

    def _check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False

            if event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                self._check_play_button(mouse_pos)
                self._up_game_level(mouse_pos)

    def _check_keydown_event(self, event):

        if event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_UP:
            self.ship.move_up = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

        elif event.key == pygame.K_RETURN:
            self._check_play_button((self.play_button.rect.x, self.play_button.rect.y))

    def _check_keyup_event(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.move_down = False
        elif event.key == pygame.K_UP:
            self.ship.move_up = False


if __name__ == "__main__":
    g = Game()
    g.run()
