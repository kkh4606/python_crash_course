from pathlib import Path
import json


class EarthquakesInfo:
    def __init__(self):

        self.generate_earth_data()

    def generate_earth_data(self):

        # Read data as a string and convert to python object
        path = Path("eq_data_30_day_m1.geojson")
        contents = path.read_text(encoding="utf-8")

        all_eq_data = json.loads(contents)

        self.title = all_eq_data["metadata"]["title"]

        self.mags, self.lons, self.lats, self.eq_titles = [], [], [], []

        all_eq_dicts = all_eq_data["features"]

        for eq_dict in all_eq_dicts:
            mag = eq_dict["properties"]["mag"]
            lon = eq_dict["geometry"]["coordinates"][0]
            lat = eq_dict["geometry"]["coordinates"][1]
            eq_title = eq_dict["properties"]["title"]
            self.mags.append(mag)
            self.lons.append(lon)
            self.lats.append(lat)
            self.eq_titles.append(eq_title)


eq_info = EarthquakesInfo()


mags, lons, lats, eq_titles, title = (
    eq_info.mags,
    eq_info.lons,
    eq_info.lats,
    eq_info.eq_titles,
    eq_info.title,
)
