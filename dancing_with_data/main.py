import matplotlib.pyplot as plt

numbers = range(1, 1001)
squares = [x**2 for x in numbers]


plt.style.use("Solarize_Light2")

fig, ax = plt.subplots()

ax.plot(numbers, squares, linewidth=1)

ax.scatter(numbers, squares, s=10, color="red")

# add titles and label

ax.set_title("Square Number Graph", fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares", fontsize=14)

# ax.tick_params(labelsize=10)

ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style="plain")


plt.show()
