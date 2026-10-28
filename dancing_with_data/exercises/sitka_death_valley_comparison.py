import csv

import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

sitka_csv = Path("w_data/sitka_weather_2021_full.csv")
death_valley_csv = Path("w_data/death_valley_2021_full.csv")

lines_sitka = sitka_csv.read_text().splitlines()
lines_death_valley = death_valley_csv.read_text().splitlines()


reader_sitka = csv.reader(lines_sitka)
next(reader_sitka)

reader_death_valley = csv.reader(lines_death_valley)
header_row = next(reader_death_valley)


dates, max_temp_sitka, max_temp_death_valley = [], [], []


for row1, row2 in zip(reader_sitka, reader_death_valley):

    current_date = datetime.strptime(row1[2], "%Y-%m-%d")

    try:

        max_temp_row1 = int(row1[7])
        max_temp_row2 = int(row2[6])

    except ValueError:

        print(f"No data for {current_date}")

    else:

        dates.append(current_date)

        max_temp_sitka.append(max_temp_row1)
        max_temp_death_valley.append(max_temp_row2)


fig, ax = plt.subplots()

ax.plot(dates, max_temp_death_valley, color="blue", alpha=0.5)
ax.plot(dates, max_temp_sitka, color="red", alpha=0.5)
ax.fill_between(dates, max_temp_death_valley, max_temp_sitka, alpha=0.1)


# Format plots

ax.set_title("Max Temperatures in Sitka and Death Valley", fontsize=20)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)

ax.tick_params(labelsize=14)


plt.show()
