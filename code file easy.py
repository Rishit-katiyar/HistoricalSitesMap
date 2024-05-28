import folium

def add_markers(map, sites):
    """Add markers for historical sites to the map."""
    for site in sites:
        name, lat, lon = site
        folium.Marker(
            location=[lat, lon],
            popup=name,
        ).add_to(map)

# Create a base map
base_map = folium.Map(location=[30.0, 70.0], zoom_start=3)

# List of historical sites with coordinates
historical_sites = [
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

# Add markers to the base map
add_markers(base_map, historical_sites)

# Save the map to an HTML file
base_map.save("historical_sites_map.html")

# Display the map
base_map
