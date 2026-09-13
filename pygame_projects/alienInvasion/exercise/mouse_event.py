import pygame

pygame.init()


class Button:

    def __init__(self, parent, msg="Play"):

        self.msg = msg

        self.screen = parent.screen

        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, 100, 30)
        self.rect.center = self.screen_rect.center
        self.button_bg_color = (0, 135, 0)
        self.button_text_color = (255, 255, 255)

        self.font = pygame.font.Font(None, 30)

        self._pre_msg(self.msg)

    def _pre_msg(self, msg):

        self.display_text = self.font.render("Play", True, self.button_text_color)

        self.display_text_rect = self.display_text.get_rect()
        self.display_text_rect.center = self.rect.center

    def draw_button(self):

        self.screen.fill(self.button_bg_color, self.rect)
        self.screen.blit(self.display_text, self.display_text_rect)


class Main:

    def __init__(self):

        self.screen = pygame.display.set_mode((300, 300))

        self.clock = pygame.time.Clock()

        self.button = Button(self)

        self.running = True

    def run(self):

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if self.button.rect.collidepoint(mouse_pos):
                        print(mouse_pos)

            self.button.draw_button()

            pygame.display.flip()


g = Main()
g.run()
