class Settings:

    def __init__(self):

        # Screen settings
        self.screen_width = 400
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # game fps
        self.fps = 60

        # board settings
        self.board_width = 130
        self.board_height = 20
        self.board_color = (51, 51, 225)
        self.board_speed = 4

        # ball settings
        self.ball_width = 20
        self.ball_height = 20
        self.ball_color = (255, 0, 0)
        self.ball_speed_x = 3
        self.ball_speed_y = 3
        self.ball_direction = 1

        # button settings
        self.button_width = 140
        self.button_height = 30
        self.button_color = "#4D694E"


settings = Settings()
