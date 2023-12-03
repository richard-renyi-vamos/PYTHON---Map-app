import webbrowser
import tkinter as tk

def open_google_maps():
    city = city_entry.get()
    if city:
        url = f"https://www.google.com/maps/place/{city}"
        webbrowser.open_new_tab(url)

# Create the GUI window
root = tk.Tk()
root.title("City Viewer")

# Create and place widgets
label = tk.Label(root, text="Enter a city:")
label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

show_button = tk.Button(root, text="Show on Google Maps", command=open_google_maps)
show_button.pack()

# Start the GUI loop
root.mainloop()
