import matplotlib.pyplot as plt


from random_walk import RandomWalk

while True:

    random_walk = RandomWalk(50_000)
    random_walk.fill_walk()

    x_values = random_walk.x_values
    y_values = random_walk.y_values
    point_numbers = range(random_walk.num_points)

    fig, ax = plt.subplots(figsize=(10, 6))

    plt.style.use("classic")
    ax.scatter(
        x_values, y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=1
    )

    # Emphasize the first and last points
    ax.scatter(0, 0, color="red", edgecolors="none", s=100)
    ax.scatter(x_values[-1], y_values[-1], color="green", edgecolors="none", s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_aspect("equal")

    plt.show()

    keep_running = input("Make another walk?(Y/N): ").lower()

    if keep_running == "y":
        break
