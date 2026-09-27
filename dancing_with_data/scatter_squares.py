import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


fig, ax = plt.subplots()

# ax.plot(x_values, y_values)
ax.scatter(x_values, y_values, c=y_values, s=10, cmap=plt.cm.Reds)


# titles and labels
ax.set_title("Square Numbers")
ax.set_xlabel("Values")
ax.set_ylabel("Squares of values")

ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style="plain")


plt.savefig("squares.png", bbox_inches="tight")
plt.show()
