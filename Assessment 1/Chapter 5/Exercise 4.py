import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.id = 0
        self.salary = 0.0

    def setData(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

    def getData(self):
        return f"{self.name}\t\t{self.position}\t{self.salary}\t{self.id}"

class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Information App")

        # Create a list to store employee objects
        self.employees = []

        # Ask the user to enter details of 5 employees
        for _ in range(5):
            self.add_employee()

        # Display employee information button
        tk.Button(self.root, text="Display Employee Information", command=self.display_employees).pack()

    def add_employee(self):
        # Create a new employee object
        employee = Employee()

        # Ask user to enter details for the employee
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        id = int(input("Enter employee ID: "))
        salary = float(input("Enter employee salary: "))

        # Set data for the employee
        employee.setData(name, age, id, salary)

        # Add the employee to the list
        self.employees.append(employee)

    def display_employees(self):
        # Create a Tkinter window to display employee information
        info_window = tk.Toplevel(self.root)
        info_window.title("Employee Information")

        # Header labels
        tk.Label(info_window, text="Name").grid(row=0, column=0)
        tk.Label(info_window, text="Position").grid(row=0, column=1)
        tk.Label(info_window, text="Salary").grid(row=0, column=2)
        tk.Label(info_window, text="ID").grid(row=0, column=3)

        # Display employee information
        for i, employee in enumerate(self.employees, start=1):
            # You can customize the position based on your requirements
            position = ["Manager", "Accountant", "Social Media", "Salesman", "Clerk"][i - 1]
            
            tk.Label(info_window, text=employee.name).grid(row=i, column=0)
            tk.Label(info_window, text=position).grid(row=i, column=1)
            tk.Label(info_window, text=employee.salary).grid(row=i, column=2)
            tk.Label(info_window, text=employee.id).grid(row=i, column=3)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()