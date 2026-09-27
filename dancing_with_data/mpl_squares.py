import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


# plt.style.use("classic")
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=10)


ax.plot(x_values, y_values, linewidth=2)


ax.set_title("Squares Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of Value", fontsize=14)

# ax.tick_params(labelsize=14)

ax.axis([0, 1100, 0, 1_100_000])

plt.show()
