from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures

dates, highs = [], []


for row in reader:

    current_date = datetime.strptime(row[2], "%Y-%m-%d")

    try:

        high = int(row[4])
    except ValueError:
        pass
    else:

        dates.append(current_date)
        highs.append(high)


# Plot the high temperatures

fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")


# Format plot
ax.set_title("Daily High Temperatures 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)

ax.tick_params(labelsize=10)


plt.show()
