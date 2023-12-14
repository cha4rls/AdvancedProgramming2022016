import tkinter as tk
from tkinter import filedialog
from collections import Counter

class StringCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("String Counter App")

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Button to select file
        tk.Button(self.root, text="Select File", command=self.select_file).pack(pady=10)

        # Display results
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select sentences file", filetypes=[("Text Files", "*.txt")])

        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()

                strings_to_search = [
                    "Hello my name is Peter Parker",
                    "I love Python Programming",
                    "Love",
                    "Enemy"
                ]

                # Count occurrences of each string
                occurrences = Counter(content.split())

                result_message = "\n".join([f"{string}: {occurrences[string]}" for string in strings_to_search])

                self.result_label.config(text=result_message)
            except Exception as e:
                self.result_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StringCounterApp(root)
    root.mainloop()