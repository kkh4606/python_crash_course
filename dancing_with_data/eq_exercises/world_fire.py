import plotly.express as px

import csv
from pathlib import Path

path = Path("world_fires_1_day.csv")

lines = path.read_text().splitlines()


reader = csv.reader(lines)
header_row = next(reader)


lats, longs, brights = [], [], []

for row in reader:

    try:
        lat = float(row[0])
        lon = float(row[1])
        bright = int(row[2])

    except ValueError:
        pass

    else:
        lats.append(lat)
        longs.append(lon)
        brights.append(bright)


title = "Global Wildfire Activity"

fig = px.scatter_geo(
    lat=lats,
    lon=longs,
    size=brights,
    color=brights,
    title=title,
    labels={"color": "Brightness"},
    color_continuous_scale="viridis",
    projection="natural earth",
)

fig.show()
