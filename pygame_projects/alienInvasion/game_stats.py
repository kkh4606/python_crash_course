class GameStats:
    """Track statics for Alien Invasion"""

    def __init__(self, root):

        self.settings = root.settings

        self.reset_stats()

    def reset_stats(self):

        self.ships_left = self.settings.ship_limit
