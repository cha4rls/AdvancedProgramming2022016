import tkinter as tk
from tkinter import ttk

class ArithmeticOperations:
    def __init__(self):
        self.result = 0

    def calculate(self, operation, value1, value2):
        try:
            num1 = float(value1)
            num2 = float(value2)

            if operation == "Addition":
                self.result = num1 + num2
            elif operation == "Subtraction":
                self.result = num1 - num2
            elif operation == "Multiplication":
                self.result = num1 * num2
            elif operation == "Division":
                if num2 != 0:
                    self.result = num1 / num2
                else:
                    return "Cannot divide by zero"
        except ValueError:
            return "Invalid input. Please enter numeric values."
        return f"Result: {self.result:.2f}"

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Calculator")

        # Create ArithmeticOperations object
        self.arithmetic_operations = ArithmeticOperations()

        # Create Combobox for selecting operation
        self.operation_var = tk.StringVar()
        operations = ["Addition", "Subtraction", "Multiplication", "Division"]
        operation_combobox = ttk.Combobox(self.root, textvariable=self.operation_var, values=operations)
        operation_combobox.grid(row=0, column=0, padx=10, pady=10)
        operation_combobox.set("Addition")

        # Create entry widgets for input values
        tk.Label(self.root, text="Enter Value 1:").grid(row=1, column=0, padx=10, pady=5)
        self.value1_var = tk.StringVar()
        entry_value1 = tk.Entry(self.root, textvariable=self.value1_var)
        entry_value1.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Enter Value 2:").grid(row=2, column=0, padx=10, pady=5)
        self.value2_var = tk.StringVar()
        entry_value2 = tk.Entry(self.root, textvariable=self.value2_var)
        entry_value2.grid(row=2, column=1, padx=10, pady=5)

        # Button to perform calculation
        tk.Button(self.root, text="Calculate", command=self.perform_calculation).grid(row=3, column=0, columnspan=2, pady=10)

        # Result label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def perform_calculation(self):
        operation = self.operation_var.get()
        value1 = self.value1_var.get()
        value2 = self.value2_var.get()

        result = self.arithmetic_operations.calculate(operation, value1, value2)

        # Update the result label
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()