import tkinter as tk
from tkinter import ttk

class ShapeDrawerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Drawer App")

        # Canvas for drawing shapes
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Combobox to select shapes
        shapes = ["Oval", "Rectangle", "Square", "Triangle"]
        self.shape_var = tk.StringVar()
        self.shape_var.set(shapes[0])
        shape_combobox = ttk.Combobox(self.root, textvariable=self.shape_var, values=shapes)
        shape_combobox.pack()

        # Button to draw the selected shape
        tk.Button(self.root, text="Draw Shape", command=self.draw_shape).pack()

    def draw_shape(self):
        shape = self.shape_var.get()

        if shape == "Oval":
            self.draw_oval()
        elif shape == "Rectangle":
            self.draw_rectangle()
        elif shape == "Square":
            self.draw_square()
        elif shape == "Triangle":
            self.draw_triangle()

    def draw_oval(self):
        self.canvas.create_oval(50, 50, 250, 150, fill="blue")

    def draw_rectangle(self):
        self.canvas.create_rectangle(50, 50, 250, 150, fill="green")

    def draw_square(self):
        self.canvas.create_rectangle(50, 50, 150, 150, fill="red")

    def draw_triangle(self):
        self.canvas.create_polygon(50, 150, 250, 150, 150, 50, fill="orange")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawerApp(root)
    root.mainloop()