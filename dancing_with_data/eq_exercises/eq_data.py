import json
from pathlib import Path
import plotly.express as px


def generate_eq_data():

    path = Path("eq.json")

    contents = path.read_text()

    all_eq_data = json.loads(contents)

    eq_title = all_eq_data["metadata"]["title"]

    mags, lons, lats, places = [], [], [], []

    all_eq_lists = all_eq_data["features"]

    for eq_dict in all_eq_lists:

        try:
            place = eq_dict["properties"]["title"]
            mag = eq_dict["properties"]["mag"]
            lon = eq_dict["geometry"]["coordinates"][0]
            lat = eq_dict["geometry"]["coordinates"][1]

        except ValueError:
            pass

        else:
            mags.append(mag)
            lons.append(lon)
            lats.append(lat)
            places.append(place)

    return mags, lons, lats, places, eq_title


mags, lons, lats, places, title = generate_eq_data()


fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    title=title,
    size=mags,
    color=mags,
    color_continuous_scale="blues",
    labels={"color": "magnitude"},
    hover_name=places,
)

fig.show()
