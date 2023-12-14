import tkinter as tk
from tkinter import messagebox, ttk, PhotoImage

# Create main window
main = tk.Tk()
main.title("Exercise2-Chapter3")

# Create images on top of the window
image_1 = PhotoImage(file="Chapter 3/latte.png", width=150, height=150)
image_2 = PhotoImage(file="Chapter 3/espresso.png", width=150, height=150)
image_3 = PhotoImage(file="Chapter 3/cappuccino.png", width=150, height=150)
image_4 = PhotoImage(file="Chapter 3/black coffee.png", width=150, height=150)
image_1label = ttk.Label(main, image=image_1)
image_2label = ttk.Label(main, image=image_2)
image_3label = ttk.Label(main, image=image_3)
image_4label = ttk.Label(main, image=image_4)
image_1label.grid(row=0, column=0, padx=5, pady=5)
image_2label.grid(row=0, column=1, padx=5, pady=5)
image_3label.grid(row=0, column=2, padx=5, pady=5)
image_4label.grid(row=0, column=3, padx=5, pady=5)

# Define coffee options
coffeeoptions = [
    "Cappuccino",
    "Flat White",
    "Spanish Latte",
    "Black Coffee",
]

# Define additional options
additionaloptions = [
    "Add Sugar",
    "No Sugar",
    "Add Milk",
    "No Milk",
    "None",
]

def selection():
    selectedcoffee = coffee.get()
    selectedadditional = additional.get()

    if selectedcoffee == "Select a Coffee" or selectedadditional == "Select Additional":
        messagebox.showerror("Error", "Please select a coffee and an option.")
    else:
        messagebox.showinfo("Order Details", f"Coffee: {selectedcoffee}\nAdditional Options: {selectedadditional}")



# Create coffee selection drop-down menu
coffee = tk.StringVar(main)
coffee.set("Select a Coffee")
coffeemenu = tk.OptionMenu(main, coffee, *coffeeoptions)
coffeemenu.grid(row=1, column=2, padx=5, pady=5)

# Create additional options drop-down menu
additional = tk.StringVar(main)
additional.set("Select Additional")
additionaloptionsmenu = tk.OptionMenu(main, additional, *additionaloptions)
additionaloptionsmenu.grid(row=2, column=2, padx=5, pady=5)


# Create order button
orderbutton = tk.Button(main, text="Order", command=selection)
orderbutton.grid(row=3, column=2, padx=5, pady=5)





# Run the gui
main.mainloop()