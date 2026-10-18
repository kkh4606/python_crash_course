import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set titles and labels

ax.set_title("Squares of Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of Value", fontsize=14)

ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style="plain")


plt.savefig("squares_plot.png", bbox_inches="tight")

# plt.show()
