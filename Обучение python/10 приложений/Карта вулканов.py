import folium
from folium.plugins import MarkerCluster
import pandas as pd

data = pd.read_csv("Volcanoes_USA.txt")
lat = data['LAT'] #широта
lon = data['LON'] #долгота
elevation = data['ELEV'] #высота

def color_change(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'
    
map = folium.Map(location=[37.0902,-100.7129], zoom_start = 5, titles = "Mapbox bright")
marker_cluster = MarkerCluster().add_to(map)

for lat, lon, elevation in zip(lat, lon, elevation):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup = str(elevation) +"m", fill_color = color_change(elevation), color = "gray", fill_opacity = 0.9).add_to(marker_cluster)
    
map.save("Map_of_volcanoes_in_the_USA.html")    