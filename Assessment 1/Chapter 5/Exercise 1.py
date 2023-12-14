import tkinter as tk
from tkinter import messagebox

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def display_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nBreed: {self.breed}"

    @classmethod
    def oldest_dog_woof(cls, dog1, dog2):
        oldest_dog = dog1 if dog1.age > dog2.age else dog2
        messagebox.showinfo("Oldest Dog Woof", f"The oldest dog, {oldest_dog.name}, says: Woof!")

class DogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dog Information App")

        # Create Dog objects
        self.dog1 = Dog("Goshen", 6, "Dobermann")
        self.dog2 = Dog("Lance", 3, "Siberian Husky")

        # Display information button
        tk.Button(self.root, text="Display Dog Information", command=self.display_info).pack()

        # Woof button
        tk.Button(self.root, text="Oldest Dog Woof", command=self.oldest_dog_woof).pack()

    def display_info(self):
        info1 = self.dog1.display_info()
        info2 = self.dog2.display_info()

        messagebox.showinfo("Dog Information", f"---Dog 1---\n{info1}\n\n---Dog 2---\n{info2}")

    def oldest_dog_woof(self):
        Dog.oldest_dog_woof(self.dog1, self.dog2)

if __name__ == "__main__":
    root = tk.Tk()
    app = DogApp(root)
    root.mainloop()