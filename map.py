import folium
from folium import plugins
import numpy as np
import time

# Define your custom places with their names and coordinates
places = {
    "Place A": (12.9716, 77.5946),  # Bangalore
    "Place B": (19.0760, 72.8777)   # Mumbai
}

# Create a base map
start_location = places["Place A"]
folium_map = folium.Map(location=start_location, zoom_start=5)

# Add markers for the places
for name, coord in places.items():
    folium.Marker(location=coord, popup=name, icon=folium.Icon(color='red')).add_to(folium_map)

# Create a PolyLine to show the route
route = [places["Place A"], places["Place B"]]
folium.PolyLine(locations=route, color='blue', weight=2.5, opacity=1).add_to(folium_map)

# Create a feature group for the vehicle marker
vehicle_marker = folium.Marker(
    location=start_location,
    popup="Vehicle",
    icon=folium.Icon(color='blue', icon='car')
).add_to(folium_map)

# Generate the HTML file
folium_map.save('interactive_map.html')

# Inform the user
print("Interactive map has been created and saved as 'interactive_map.html'.")
