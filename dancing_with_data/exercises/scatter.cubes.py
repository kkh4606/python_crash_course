import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]


fig, ax = plt.subplots()


ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues)


# set titles and labels

ax.set_title("Cubes of Numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=10)
ax.set_ylabel("Cubes of Value", fontsize=10)

ax.tick_params(labelsize=9)

ax.axis([0, 5100, 0, 125_000_000_000])
ax.ticklabel_format(style="plain")


plt.show()
