


import folium
import numpy as np

# Define the historical sites with their names and coordinates
sites = [
    ("Göbekli Tepe", 37.2231, 38.9225),
    ("Tower of Jericho", 31.8667, 35.4500),
    ("Çatalhöyük", 37.6670, 32.8262),
    ("Mehrgarh", 29.3622, 67.6233),
    ("Anu ziggurat of Uruk", 31.3275, 45.6401),
    ("Dholavira", 23.8881, 70.2063),
    ("Shahr-e Sukhteh", 30.5911, 61.4067),
    ("Tepe Sialk ziggurat", 33.9686, 51.4008),
    ("Harappa", 30.6266, 72.8758),
    ("Mohenjo Daro", 27.3275, 68.1385),
    ("Royal Palace of Ebla", 35.7975, 36.7950),
    ("Shimao", 37.6462, 110.0508),
    ("Ziggurat of Ur", 30.9625, 46.1033),
    ("Sinauli", 29.2320, 77.2387),
    ("Adichanallur", 8.7150, 77.7247),
    ("Ziggurat of Dur-Kurigalzu", 33.3208, 44.0500),
    ("Chogha Zanbil", 32.0145, 48.5225),
    ("Van Fortress", 38.5021, 43.3795),
    ("Keezhadi excavation site", 9.7481, 78.1856),
    ("Tomb of Cyrus", 30.1992, 53.1778),
    ("Persepolis", 29.9351, 52.8910),
    ("Sanchi Stupa", 23.4793, 77.7398),
    ("Dhamek Stupa", 25.3724, 83.0222),
    ("Mausoleum of the First Qin Emperor", 34.3846, 109.2787),
    ("Ruwanwelisaya", 8.3498, 80.3964),
    ("Masada", 31.3156, 35.3525),
    ("Lei Cheng Uk Han Tomb Museum", 22.3394, 114.1628),
    ("Temple of Garni", 40.1123, 44.7294),
]

# Convert the sites to a dictionary for easy access
site_dict = {site[0]: (site[1], site[2]) for site in sites}

# Define more complex paths between sites with multiple checkpoints representing valleys, passes, or ancient cities
paths = {
    ("Göbekli Tepe", "Tower of Jericho"): [
        ("Euphrates River", 36.55, 38.2667),
        ("Aleppo", 36.2021, 37.1343),
        ("Damascus", 33.5138, 36.2765),
        ("Jericho", 31.8667, 35.4500),
        ("Jordan River", 32.1943, 35.4521),
        ("Amman", 31.9539, 35.9106),
    ],
    ("Göbekli Tepe", "Çatalhöyük"): [
        ("Malatya", 38.3489, 38.3335),
        ("Euphrates River", 37.1083, 38.7858),
        ("Seyhan River", 37.0, 35.3213),
        ("Konya", 37.8746, 32.4932),
    ],
    ("Çatalhöyük", "Mehrgarh"): [
        ("Tigris River", 37.1053, 40.7787),
        ("Mosul", 36.3309, 43.1053),
        ("Baghdad", 33.3152, 44.3661),
        ("Tehran", 35.6892, 51.3890),
        ("Zahedan", 29.4978, 60.8723),
    ],
    ("Mehrgarh", "Harappa"): [
        ("Sibi", 29.5549, 67.8760),
        ("Indus River", 27.9272, 68.7513),
        ("Rohri", 27.6926, 68.8951),
        ("Multan", 30.1575, 71.5249),
    ],
    ("Harappa", "Mohenjo Daro"): [
        ("Hyderabad", 25.3960, 68.3578),
        ("Indus River", 24.7681, 67.0236),
    ],
    ("Anu ziggurat of Uruk", "Ziggurat of Ur"): [
        ("Euphrates River", 30.9546, 46.1022),
    ],
    ("Ziggurat of Ur", "Ziggurat of Dur-Kurigalzu"): [
        ("Euphrates River", 32.0301, 45.3131),
    ],
    ("Ziggurat of Dur-Kurigalzu", "Chogha Zanbil"): [
        ("Tigris River", 32.3825, 47.9753),
        ("Ahvaz", 31.3203, 48.6692),
    ],
    ("Shahr-e Sukhteh", "Tepe Sialk ziggurat"): [
        ("Isfahan", 32.6546, 51.6680),
    ],
    ("Tepe Sialk ziggurat", "Persepolis"): [
        ("Shiraz", 29.5918, 52.5836),
    ],
    ("Persepolis", "Tomb of Cyrus"): [],
    ("Royal Palace of Ebla", "Masada"): [
        ("Amman", 31.9539, 35.9106),
        ("Jordan River", 31.9, 35.6),
    ],
    ("Sinauli", "Keezhadi excavation site"): [
        ("Nagpur", 21.1458, 79.0882),
        ("Godavari River", 19.3, 77.2),
    ],
    ("Keezhadi excavation site", "Adichanallur"): [],
    ("Sanchi Stupa", "Dhamek Stupa"): [
        ("Narmada River", 22.4758, 72.8937),
    ],
    ("Mausoleum of the First Qin Emperor", "Shimao"): [
        ("Yellow River", 34.0, 109.0),
    ],
}

# Create a base map centered at an average location
map_center = [30.0, 70.0]
map = folium.Map(location=map_center, zoom_start=3)

# Add markers for each site
for site in sites:
    folium.Marker(location=[site[1], site[2]], popup=site[0]).add_to(map)

# Function to create waypoints between two coordinates
def interpolate_points(start, end, num_points=100):
    lat_points = np.linspace(start[0], end[0], num_points)
    lon_points = np.linspace(start[1], end[1], num_points)
    return list(zip(lat_points, lon_points))

# Function to manually adjust paths to follow known valleys, rivers, and avoid mountains
def adjust_path(start, end, checkpoints):
    path = [start]
    for checkpoint in checkpoints:
        path.append((checkpoint[1], checkpoint[2]))
    path.append(end)

    adjusted_path = []
    for i in range(len(path) - 1):
        segment = interpolate_points(path[i], path[i + 1])
        adjusted_path.extend(segment)
    return adjusted_path

# Add paths to the map
for (start_site, end_site), checkpoints in paths.items():
    start = site_dict[start_site]
    end = site_dict[end_site]
    adjusted_path = adjust_path(start, end, checkpoints)
    folium.PolyLine(locations=adjusted_path, color='blue').add_to(map)

# Add trade paths between sites
trade_paths = {
    ("Göbekli Tepe", "Tower of Jericho"): [
        ("Trade Point 1", 36.1, 37.5),
        ("Trade Point 2", 34.8, 36.9),
        ("Trade Point 3", 35.5, 37.2),
        ("Trade Point 4", 34.2, 36.6),
    ],
    ("Çatalhöyük", "Mehrgarh"): [
        ("Trade Point 3", 37.5, 39.5),
        ("Trade Point 4", 35.7, 42.1),
        ("Trade Point 5", 36.2, 40.8),
        ("Trade Point 6", 35.1, 41.5),
    ],
    ("Harappa", "Mohenjo Daro"): [
        ("Trade Point 5", 26.5, 67.7),
        ("Trade Point 6", 25.1, 66.5),
        ("Trade Point 7", 25.8, 67.3),
        ("Trade Point 8", 26.2, 66.9),
    ],
    ("Royal Palace of Ebla", "Masada"): [
        ("Trade Point 7", 34.7, 36.0),
        ("Trade Point 8", 32.2, 35.8),
        ("Trade Point 9", 33.5, 35.9),
        ("Trade Point 10", 32.8, 35.6),
    ],
}

# Add trade paths to the map
for (start_site, end_site), trade_points in trade_paths.items():
    for point in trade_points:
        folium.CircleMarker(location=[point[1], point[2]], radius=5, color='green', fill=True, fill_color='green').add_to(map)

# Add legends
legend_html = '''
     <div style="position: fixed; 
     bottom: 50px; left: 50px; width: 150px; height: 90px; 
     border:2px solid grey; z-index:9999; font-size:14px;
     background-color:white; opacity: 0.8;
     ">
     <p style="margin: 10px;"> <b>Legends</b> </p>
     <p style="margin: 5px;"><i class="fa fa-circle" style="color:green"></i> Trade Path Points</p>
     <p style="margin: 5px;"><i class="fa fa-circle" style="color:blue"></i> Historical Paths</p>
      </div>
     '''
map.get_root().html.add_child(folium.Element(legend_html))

# Save the map to an HTML file
map.save("historical_sites_map.html")

# Display the map
map
