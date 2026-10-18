import matplotlib.pyplot as plt
from dancing_with_data.random_walk import RandomWalk

random_walk = RandomWalk(points=5000)
random_walk.fill_walk()


fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

ax.plot(random_walk.x_values, random_walk.y_values, linewidth=3)


plt.show()
