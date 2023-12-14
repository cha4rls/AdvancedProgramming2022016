import tkinter as tk
from tkinter import messagebox

class BioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bio Information App")

        # Entry variables
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.hometown_var = tk.StringVar()

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widgets
        tk.Label(self.root, text="Name:").grid(row=0, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(self.root, text="Age:").grid(row=1, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.age_var).grid(row=1, column=1)

        tk.Label(self.root, text="Hometown:").grid(row=2, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.hometown_var).grid(row=2, column=1)

        # Buttons
        tk.Button(self.root, text="Save to File", command=self.save_to_file).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Read from File", command=self.read_from_file).grid(row=4, column=0, columnspan=2, pady=10)

    def save_to_file(self):
        try:
            with open("bio.txt", "w") as file:
                file.write(f"Name: {self.name_var.get()}\n")
                file.write(f"Age: {self.age_var.get()}\n")
                file.write(f"Hometown: {self.hometown_var.get()}\n")
            messagebox.showinfo("Success", "Data has been saved to bio.txt.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def read_from_file(self):
        try:
            with open("bio.txt", "r") as file:
                content = file.read()
            messagebox.showinfo("Bio Information", content)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found. Save data first.")

if __name__ == "__main__":
    root = tk.Tk()
    bio_app = BioApp(root)
    root.mainloop()