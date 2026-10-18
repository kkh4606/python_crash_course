from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_07-2021_simple.csv")

lines = path.read_text().splitlines()


reader = csv.reader(lines)

header_row = next(reader)


highs = [int(row[4]) for row in reader]


# Plot the high temperatures .


fig, ax = plt.subplots()

ax.plot(highs, color="red")

# Format plot.
ax.set_title("Daily High Tempratures, July 2021", fontsize=24)

ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
