import matplotlib.pyplot as plt
import csv
from pathlib import Path
from datetime import datetime


class GenerateTemperature:

    def __init__(self, path):
        self.dates, self.highs, self.lows = [], [], []

        self.path = Path(path)
        self.title = None

    def generate(self):

        lines = self.path.read_text().splitlines()

        reader = csv.reader(lines)

        header_row = next(reader)

        for r in reader:

            title = r[header_row.index("NAME")]

            self.title = title
            break

        for row in reader:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")

            try:

                high = int(row[header_row.index("TMAX")])
                low = int(row[header_row.index("TMIN")])

            except ValueError:
                print(f"No data for {current_date}")
            else:
                self.dates.append(current_date)
                self.highs.append(high)
                self.lows.append(low)


t = GenerateTemperature("w_data/4423131.csv")
t.generate()


fig, ax = plt.subplots()
ax.plot(t.dates, t.highs, color="red", alpha=0.5)
ax.plot(t.dates, t.lows, color="blue", alpha=0.5)
ax.fill_between(t.dates, t.highs, t.lows, color="green", alpha=0.1)


# Format plots
ax.set_title(t.title, fontsize=20)
ax.set_xlabel("", fontsize=13)

fig.autofmt_xdate()
ax.set_ylabel("Temperatures (F)")

ax.tick_params(labelsize=15)


plt.show()
