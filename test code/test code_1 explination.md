



# Detailed Explanation of Python Code: Adding Historical Site Markers on a Map

## Importing Folium Library

```python
import folium
```

The code begins by importing the Folium library, which is a Python wrapper for Leaflet.js, a popular library for creating interactive maps.

## Defining the Function to Add Markers

```python
def add_markers(map, sites):
    """Add markers for historical sites to the map."""
    for site in sites:
        name, lat, lon = site
        folium.Marker(
            location=[lat, lon],
            popup=name,
        ).add_to(map)
```

Next, a function named `add_markers` is defined. This function takes two parameters: `map` (a Folium Map object) and `sites` (a list of historical sites with their coordinates). Inside the function, it iterates over each historical site, extracts its name, latitude, and longitude from the tuple, and then creates a Folium Marker object with the given location and popup text (name of the site). Finally, it adds the marker to the map.

## Creating a Base Map

```python
base_map = folium.Map(location=[30.0, 70.0], zoom_start=3)
```

A base map is created using the `folium.Map()` function. The `location` parameter specifies the initial center of the map, and `zoom_start` sets the initial zoom level.

## List of Historical Sites

```python
historical_sites = [
    ("Göbekli Tepe", 37.2231, 38.9225),
    ("Tower of Jericho", 31.8667, 35.4500),
    ...
]
```

This is a list containing tuples, with each tuple representing a historical site. Each tuple contains the name of the site, its latitude, and longitude.

## Adding Markers to the Base Map

```python
add_markers(base_map, historical_sites)
```

The `add_markers` function is called to add markers for all historical sites to the base map.

## Saving the Map to HTML File

```python
base_map.save("historical_sites_map.html")
```

Finally, the base map with added markers is saved to an HTML file named "historical_sites_map.html".

## Displaying the Map

```python
base_map
```

This line would typically display the map in a Jupyter Notebook or an interactive Python environment, allowing users to interact with it.
