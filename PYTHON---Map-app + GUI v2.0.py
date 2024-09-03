import tkinter as tk
import folium
import webbrowser

def create_map(lat, lon, zoom_level):
    # Create a map centered at the given latitude and longitude
    my_map = folium.Map(location=[lat, lon], zoom_start=zoom_level)
    
    # Add a marker
    folium.Marker([lat, lon], tooltip="Marker").add_to(my_map)
    
    # Save the map as an HTML file
    map_file = "my_map.html"
    my_map.save(map_file)
    
    # Open the map in the default web browser
    webbrowser.open(map_file)

def on_submit():
    # Get the user input values
    lat = float(entry_lat.get())
    lon = float(entry_lon.get())
    zoom_level = int(entry_zoom.get())
    
    # Create and display the map
    create_map(lat, lon, zoom_level)

# Create the main window
root = tk.Tk()
root.title("Python Map App")

# Create and place the input fields and labels
label_lat = tk.Label(root, text="Latitude:")
label_lat.pack()
entry_lat = tk.Entry(root)
entry_lat.pack()

label_lon = tk.Label(root, text="Longitude:")
label_lon.pack()
entry_lon = tk.Entry(root)
entry_lon.pack()

label_zoom = tk.Label(root, text="Zoom Level:")
label_zoom.pack()
entry_zoom = tk.Entry(root)
entry_zoom.pack()

# Create the submit button
submit_button = tk.Button(root, text="Create Map", command=on_submit)
submit_button.pack()

# Run the application
root.mainloop()
