import csv

import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

path = Path.cwd().resolve().parent / "weather_data/sitka_weather_2021_full.csv"

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, prcps = [], []


for row in reader:
    print(row)
    current_date = datetime.strptime(row[2], "%Y-%m-%d")

    try:
        prcp = float(row[5])
        # high = int(row[7])
        # low = int(row[8])

    except ValueError:
        print(f"No data for {current_date}")

    else:

        dates.append(current_date)
        prcps.append(prcp)


fig, ax = plt.subplots()

ax.plot(dates, prcps, color="green", alpha=0.5)

# Format plots

ax.set_title("Daily Rainfall Amounts, 2021", fontsize=24)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("PRCP")


plt.show()
