import matplotlib.pyplot as plt
import csv
from pathlib import Path
from datetime import datetime


def generate_temps():

    path = Path("w_data/4422482.csv")
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)

    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:

        try:

            current_date = datetime.strptime(row[2], "%Y-%m-%d")

            high = int(row[4])
            low = int(row[5])
        except ValueError:
            ...

        else:

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


dates, highs, lows = generate_temps()


fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)


# Format plots
ax.set_title("Daily High and Low Temperatures San Francisco", fontsize=20)
ax.set_xlabel("", fontsize=13)

fig.autofmt_xdate()
ax.set_ylabel("Temperatures (F)")

ax.tick_params(labelsize=15)


plt.show()
