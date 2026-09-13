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


class Levels:
    def __init__(self):

        self.easy = 1
        self.medium = 1.1
        self.hard = 2


class Buttons:
    def __init__(self, parent):

        self.screen = parent.screen

        self.settings = parent.settings

        self.play_rect = pygame.Rect(375, 280, 150, 40)
        self.easy_rect = pygame.Rect(375, 330, 150, 40)
        self.medium_rect = pygame.Rect(375, 380, 150, 40)
        self.hard_rect = pygame.Rect(375, 430, 150, 40)

        self.font = pygame.font.Font(None, 30)

        self._prep_text()

    def _prep_text(self):

        self.play_msg = self.font.render("Play", True, "white")
        self.play_msg_rect = self.play_msg.get_rect()

        self.easy_msg = self.font.render("Easy", True, "white")
        self.easy_msg_rect = self.easy_msg.get_rect()

        self.medium_msg = self.font.render("Medium", True, "white")
        self.medium_msg_rect = self.medium_msg.get_rect()

        self.hard_msg = self.font.render("Hard", True, "white")
        self.hard_msg_rect = self.medium_msg.get_rect()

        self.play_msg_rect.center = self.play_rect.center
        self.easy_msg_rect.center = self.easy_rect.center
        self.medium_msg_rect.center = self.medium_rect.center
        self.hard_msg_rect.center = self.hard_rect.center

    def draw(self):
        self.screen.fill("green", self.play_rect)
        self.screen.fill("green", self.easy_rect)
        self.screen.fill("green", self.medium_rect)
        self.screen.fill("green", self.hard_rect)

        self.screen.blit(self.play_msg, self.play_msg_rect)
        self.screen.blit(self.easy_msg, self.easy_msg_rect)
        self.screen.blit(self.medium_msg, self.medium_msg_rect)
        self.screen.blit(self.hard_msg, self.hard_msg_rect)


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

        self.rect = pygame.Rect(0, 0, self.settings.width, self.settings.height)

        self.rect.y = self.screen_rect.center[1]

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
        self.buttons = Buttons(self)

        self.stats = ResetStats(self)
        self.clock = pygame.time.Clock()
        self.game_active = False
        self.running = True

    def run(self):

        while self.running:

            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.buttons.play_rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:

            self.stats.reset_stats()
            self.game_active = True

            self.bullets.empty()
            self.enemy.reset_position()
            self.ship.reset_position()

            pygame.mouse.set_visible(False)

    def _update_enemy(self):
        self._check_rect_edge()
        self.enemy.update()

    def _check_rect_edge(self):
        if self.enemy.check_edge():

            self._change_direction()

    def _change_direction(self):

        self.settings.rect_direction *= -1

    def _show_fps(self):

        font = pygame.font.SysFont("consolas", 18)

        fps = pygame.time.Clock.get_fps(self.clock)

        fps_image = font.render(f"FPS:{fps:.2f}", True, "green")

        self.screen.blit(fps_image, (3, 7))

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
        self.ship.blitme()

        if not self.game_active:

            self.buttons.draw()

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

    def _check_keydown_event(self, event):

        if event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_UP:
            self.ship.move_up = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

        elif event.key == pygame.K_RETURN:
            self._check_play_button(
                (self.buttons.play_rect.x, self.buttons.play_rect.y)
            )

    def _check_keyup_event(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.move_down = False
        elif event.key == pygame.K_UP:
            self.ship.move_up = False


if __name__ == "__main__":
    g = Game()
    g.run()
