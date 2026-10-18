from random import choice


class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, points=5000):

        self.num_points = points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points:

            x_step, y_step = self.get_step()

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        x_step = x_direction * x_distance

        y_direction = choice([1, 0])
        y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        y_step = y_direction * y_distance

        return x_step, y_step
