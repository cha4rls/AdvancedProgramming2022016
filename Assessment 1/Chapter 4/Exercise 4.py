import tkinter as tk
from tkinter import filedialog

class LetterCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Letter Counter App")

        # Entry variable
        self.letter_var = tk.StringVar()

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for user input
        tk.Label(self.root, text="Enter a character:").pack()
        entry_letter = tk.Entry(self.root, textvariable=self.letter_var)
        entry_letter.pack()

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

                letter_to_count = self.letter_var.get()

                # Count occurrences of the letter
                occurrences = content.count(letter_to_count)

                result_message = f"The letter '{letter_to_count}' appears {occurrences} times."

                self.result_label.config(text=result_message)
            except Exception as e:
                self.result_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LetterCounterApp(root)
    root.mainloop()
