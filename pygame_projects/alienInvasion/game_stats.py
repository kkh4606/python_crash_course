class GameStats:
    """Track statics for Alien Invasion"""

    def __init__(self, root):

        self.settings = root.settings

        self.initialize_high_score()
        self.reset_stats()

    def reset_stats(self):

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def initialize_high_score(self):
        print("initializing high score...")

        with open("highest_score.txt", "r") as f:

            self.high_score = int(f.read())
