import tkinter as tk
from tkinter import ttk, messagebox
import math

class ShapeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Calculator App")

        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)

        # Create tabs for different shapes
        self.circle_tab = ttk.Frame(self.notebook)
        self.square_tab = ttk.Frame(self.notebook)
        self.rectangle_tab = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.circle_tab, text="Circle")
        self.notebook.add(self.square_tab, text="Square")
        self.notebook.add(self.rectangle_tab, text="Rectangle")

        # GUI elements in the Circle tab
        self.create_circle_tab()

        # GUI elements in the Square tab
        self.create_square_tab()

        # GUI elements in the Rectangle tab
        self.create_rectangle_tab()

        # Pack the notebook to make it visible
        self.notebook.pack(expand=1, fill="both")

    def create_circle_tab(self):
        # Radius input
        tk.Label(self.circle_tab, text="Enter Radius:").pack()
        self.radius_var = tk.DoubleVar()
        tk.Entry(self.circle_tab, textvariable=self.radius_var).pack()

        # Button to calculate and display area
        tk.Button(self.circle_tab, text="Calculate Area", command=self.calculate_circle_area).pack()

    def calculate_circle_area(self):
        try:
            radius = self.radius_var.get()
            if radius <= 0:
                raise ValueError("Radius must be a positive number.")
            area = math.pi * radius**2
            messagebox.showinfo("Circle Area", f"The area of the circle is: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def create_square_tab(self):
        # Side length input
        tk.Label(self.square_tab, text="Enter Side Length:").pack()
        self.side_length_var = tk.DoubleVar()
        tk.Entry(self.square_tab, textvariable=self.side_length_var).pack()

        # Button to calculate and display area
        tk.Button(self.square_tab, text="Calculate Area", command=self.calculate_square_area).pack()

    def calculate_square_area(self):
        try:
            side_length = self.side_length_var.get()
            if side_length <= 0:
                raise ValueError("Side length must be a positive number.")
            area = side_length**2
            messagebox.showinfo("Square Area", f"The area of the square is: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def create_rectangle_tab(self):
        # Length and Width input
        tk.Label(self.rectangle_tab, text="Enter Length:").grid(row=0, column=0, sticky="e")
        tk.Label(self.rectangle_tab, text="Enter Width:").grid(row=1, column=0, sticky="e")

        self.length_var = tk.DoubleVar()
        self.width_var = tk.DoubleVar()

        tk.Entry(self.rectangle_tab, textvariable=self.length_var).grid(row=0, column=1)
        tk.Entry(self.rectangle_tab, textvariable=self.width_var).grid(row=1, column=1)

        # Button to calculate and display area
        tk.Button(self.rectangle_tab, text="Calculate Area", command=self.calculate_rectangle_area).grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_rectangle_area(self):
        try:
            length = self.length_var.get()
            width = self.width_var.get()

            if length <= 0 or width <= 0:
                raise ValueError("Length and width must be positive numbers.")
            area = length * width
            messagebox.showinfo("Rectangle Area", f"The area of the rectangle is: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeCalculatorApp(root)
    root.mainloop()
