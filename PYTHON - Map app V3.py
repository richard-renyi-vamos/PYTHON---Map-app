import tkinter as tk
from tkinter import messagebox
import folium
import webbrowser

def create_map(lat, lon, zoom_level, style="OpenStreetMap"):
    """
    Creates an interactive map. 
    Added 'style' parameter to allow for different visual themes (e.g., Terrain).
    """
    my_map = folium.Map(location=[lat, lon], zoom_start=zoom_level, tiles=style)
    
    # Customizing the marker to be more descriptive
    folium.Marker(
        [lat, lon], 
        popup=f"Coordinates: {lat}, {lon}",
        tooltip="Click for Info",
        icon=folium.Icon(color='green', icon='leaf') # A nod to your vegan/nature interests
    ).add_to(my_map)
    
    map_file = "my_map.html"
    my_map.save(map_file)
    webbrowser.open(map_file)

def add_nature_marker(lat, lon):
    """
    A helpful function to quickly find local green spaces or 
    quiet spots for meditation/nature walks.
    """
    # Logic could be expanded here to use an API like Google Places
    print(f"Searching for nature spots near {lat}, {lon}...")

def clear_fields():
    """Clears the input boxes for a fresh start."""
    entry_lat.delete(0, tk.END)
    entry_lon.delete(0, tk.END)
    entry_zoom.delete(0, tk.END)

def on_submit():
    try:
        # Input Validation: Ensures the app handles typos gracefully
        lat = float(entry_lat.get())
        lon = float(entry_lon.get())
        zoom_level = int(entry_zoom.get())
        
        # Using 'Stamen Terrain' for a more nature-focused view
        create_map(lat, lon, zoom_level, style="OpenStreetMap")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for coordinates and zoom.")

# --- UI Setup ---
root = tk.Tk()
root.title("Richard's Nature Map Explorer")
root.geometry("300x350") # Set a default size for better layout

# Label and Entry for Latitude
tk.Label(root, text="Latitude (e.g., 34.05):").pack(pady=2)
entry_lat = tk.Entry(root)
entry_lat.pack()

# Label and Entry for Longitude
tk.Label(root, text="Longitude (e.g., -118.24):").pack(pady=2)
entry_lon = tk.Entry(root)
entry_lon.pack()

# Label and Entry for Zoom
tk.Label(root, text="Zoom Level (1-20):").pack(pady=2)
entry_zoom = tk.Entry(root)
entry_zoom.insert(0, "12") # Default zoom value
entry_zoom.pack()

# --- Buttons ---
submit_button = tk.Button(root, text="Generate Map", command=on_submit, bg="#4CAF50", fg="white")
submit_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear Fields", command=clear_fields)
clear_button.pack()

root.mainloop()
