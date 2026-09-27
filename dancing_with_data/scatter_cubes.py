import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]


fig, ax = plt.subplots()


ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)


# titles and labels

ax.set_title("Cubes Values")
ax.set_xlabel("values")
ax.set_ylabel("Cubes of Vales")

ax.axis([0, 5500, 0, 125_000_000_000])
ax.ticklabel_format(style="plain")


plt.show()
