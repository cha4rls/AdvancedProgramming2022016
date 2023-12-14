import tkinter as tk
from tkinter import messagebox

class PasswordValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Validator App")

        # Entry variable
        self.password_var = tk.StringVar()

        # Passcode attempts
        self.attempts_remaining = 5

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for user input
        tk.Label(self.root, text="Enter Password:").pack()
        entry_password = tk.Entry(self.root, show="*", textvariable=self.password_var)
        entry_password.pack()

        # Button to validate password
        tk.Button(self.root, text="Validate Password", command=self.validate_password).pack(pady=10)

    def validate_password(self):
        password = self.password_var.get()

        if self.is_valid_password(password):
            messagebox.showinfo("Password Valid", "Password is valid!")
            self.root.destroy()
        else:
            self.attempts_remaining -= 1
            if self.attempts_remaining > 0:
                messagebox.showwarning("Invalid Password", f"Invalid password! {self.attempts_remaining} attempts remaining.")
            else:
                messagebox.showerror("Security Alert", "Invalid password! Authorities have been alerted!")
                self.root.destroy()

    def is_valid_password(self, password):
        # Password criteria
        lowercase_letter = any(char.islower() for char in password)
        uppercase_letter = any(char.isupper() for char in password)
        digit = any(char.isdigit() for char in password)
        special_char = any(char in "$#@!" for char in password)
        length_valid = 6 <= len(password) <= 12

        # Check all criteria
        return lowercase_letter and uppercase_letter and digit and special_char and length_valid

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordValidatorApp(root)
    root.mainloop()
