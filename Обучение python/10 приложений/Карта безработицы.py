import csv
import json
import folium
from folium.plugins import MarkerCluster
import pandas as pd

geo_data = json.load(open("us-states.json"))
emp_data = pd.read_csv(open("us-unemployment.csv"))

map = folium.Map(location=[37.0902,-100.7129], zoom_start = 4)

folium.Choropleth(
    geo_data=geo_data, data=emp_data,
    name = 'Unemployment Rate',
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
    legend_name='Unemployment Rate (%)'
).add_to(map)

map.save("Unemployment_rate_in_the_USA.html")