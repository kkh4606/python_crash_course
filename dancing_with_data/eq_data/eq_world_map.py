import plotly.express as px
from eq_explore_data import mags, lons, lats, eq_titles, title

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="viridis",
    labels={"color": "Magnitude"},
    # projection="natural earth",
    hover_name=eq_titles,
)
fig.show()
