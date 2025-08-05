import folium
from folium import plugins

# Define locations
places = {
    "Place A": (12.9716, 77.5946),  # Bangalore
    "Place B": (19.0760, 72.8777)   # Mumbai
}

# Create a base map centered at 'Place A'
folium_map = folium.Map(location=places["Place A"], zoom_start=5)

# Add markers for each place
for name, coord in places.items():
    folium.Marker(
        location=coord,
        popup=folium.Popup(name, max_width=300),
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(folium_map)

# Add a polyline between 'Place A' and 'Place B'
folium.PolyLine(
    locations=[places["Place A"], places["Place B"]],
    color='blue',
    weight=2.5,
    opacity=1
).add_to(folium_map)

# Add a vehicle marker at 'Place A'
folium.Marker(
    location=places["Place A"],
    popup=folium.Popup("Vehicle", max_width=300),
    icon=folium.Icon(color='blue', icon='car')
).add_to(folium_map)

# Save the map to an HTML file
folium_map.save('interactive_map.html')

print("Interactive map has been created and saved as 'interactive_map.html'.")
