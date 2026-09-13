class Settings:
    def __init__(self):

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship settings

        self.ship_limit = 3

        # bullets settings

        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20

        # alien settings

        self.fleet_drop_speed = 20

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""

        self.ship_speed = 4
        self.bullet_speed = 4
        self.alien_speed = 3.0

        # fleet_direction of 1 represents right;-1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
