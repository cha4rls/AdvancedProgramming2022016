import tkinter as tk
from tkinter import messagebox

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.Name = name
        self.Mark1 = mark1
        self.Mark2 = mark2
        self.Mark3 = mark3

    def calcGrade(self):
        return (self.Mark1 + self.Mark2 + self.Mark3) / 3

    def display(self):
        average = self.calcGrade()
        messagebox.showinfo("Student Information", f"Student Name: {self.Name}\nGrade Average: {average:.2f}")

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information App")

        # Get input from the user
        name = input("Enter student name: ")
        mark1 = int(input("Enter mark 1: "))
        mark2 = int(input("Enter mark 2: "))
        mark3 = int(input("Enter mark 3: "))

        # Create student object using constructor
        self.student1 = Students(name, mark1, mark2, mark3)

        # Button to display student information
        tk.Button(self.root, text="Display Student Information", command=self.display_info).pack()

        # Button to get user input and create another student object
        tk.Button(self.root, text="Create Another Student", command=self.create_another_student).pack()

    def display_info(self):
        self.student1.display()

    def create_another_student(self):
        name = input("Enter student name: ")
        mark1 = int(input("Enter mark 1: "))
        mark2 = int(input("Enter mark 2: "))
        mark3 = int(input("Enter mark 3: "))

        # Create another student object using constructor
        student2 = Students(name, mark1, mark2, mark3)
        student2.display()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()