import tkinter as tk
from tkinter import ttk

def update_greeting():
    name = entry_name.get()
    selected_color = color_var.get()
    greeting = f"Good day, {name}!"
    label_display.config(text=greeting, fg="black", bg=selected_color)

# Create the main window
root = tk.Tk()
root.title("Greeting App")

# Set default window size
root.geometry("700x200")

# InputFrame
input_frame = tk.Frame(root, bg="#eba81b", padx=10, pady=10)
input_frame.grid(row=0, column=0, padx=10, pady=10)

# Title label in blue
title_label = tk.Label(input_frame, text="Welcome!", font=("Helvetica", 12, "bold"), fg="white", bg="#87CEFA")
title_label.grid(row=0, column=0, columnspan=2, pady=5)

# Entry field for user's name
label_name = tk.Label(input_frame, text="Enter your name:", bg="#87CEFA")
label_name.grid(row=1, column=0, pady=5, sticky="e")

entry_name = tk.Entry(input_frame)
entry_name.grid(row=1, column=1, pady=5, padx=5, sticky="w")

# Dropdown menu for selecting color
label_color = tk.Label(input_frame, text="Select background color:", bg="#87CEFA")
label_color.grid(row=2, column=0, pady=5, sticky="e")

colors = ["red", "yellow", "green", "purple", "blue"]
color_var = tk.StringVar()
color_dropdown = ttk.Combobox(input_frame, textvariable=color_var, values=colors)
color_dropdown.set("Select")
color_dropdown.grid(row=2, column=1, pady=5, padx=5, sticky="w")

# Update Greeting button
update_button = tk.Button(input_frame, text="Enter", command=update_greeting)
update_button.grid(row=3, column=0, columnspan=2, pady=10)

# DisplayFrame
display_frame = tk.Frame(root, padx=10, pady=10)
display_frame.grid(row=0, column=1, padx=10, pady=10)

# Initially, DisplayFrame is empty
label_display = tk.Label(display_frame, text="", font=("Helvetica", 23))
label_display.pack()

# Run the Tkinter event loop
root.mainloop()