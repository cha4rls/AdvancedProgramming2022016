import tkinter as tk
from tkinter import font

def change_font():
    # Change label font style
    new_font = font.Font(label_welcome, label_welcome.cget("font"))
    new_font.config(size=16, weight="bold", family="Arial")
    label_welcome['font'] = new_font

# Create the main window
root = tk.Tk()
root.title("Welcome to GUI Program")

# Set default window size
root.geometry("400x200")

# Disable resizing the window
root.resizable(False, False)

# Add background color to the window
root.configure(bg="#e6e6e6")

# Create a label with a welcome message
welcome_message = "Welcome to GUI Program!"
label_welcome = tk.Label(root, text=welcome_message, font=("Helvetica", 14), bg="#e6e6e6")
label_welcome.pack(pady=20)

# Create a button to change the font
change_font_button = tk.Button(root, text="Change Font", command=change_font)
change_font_button.pack()

# Run the Tkinter event loop
root.mainloop()