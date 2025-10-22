import tkinter as tk
from random import choice
from string import ascii_letters, digits, punctuation
from time import sleep
from tkinter import ttk

from pyperclip import copy


class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x420")
        self.root.resizable(False, False)

        # Optional: Fade-in effect on startup
        self.root.attributes("-alpha", 0.0)
        self.fade_in()

        # Set up a style to make the UI more "modern"
        self.style = ttk.Style()
        self.style.theme_use("clam")  # or 'default', 'alt', etc.

        # General background color
        self.root.configure(bg="#f2f2f2")

        # Configure style for various ttk widgets
        # Note: Some style names (like TButton, TLabel, TFrame, etc.) are defaults
        self.style.configure(
            "TLabel", background="#f2f2f2", foreground="#333333", font=("Arial", 10)
        )
        self.style.configure(
            "TButton",
            background="#4CAF50",
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            borderwidth=0,
        )
        # Make sure Checkbuttons and Entries also adapt background
        self.style.configure("TCheckbutton", background="#f2f2f2", font=("Arial", 10))
        self.style.configure("TEntry", foreground="#333333", fieldbackground="#ffffff")

        # Create variables
        self.password_length = tk.IntVar(value=12)
        self.use_letters = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        self.create_widgets()

    def fade_in(self):
        """Simple fade-in animation for the root window."""
        for i in range(0, 101, 4):  # Adjust step for speed
            self.root.attributes("-alpha", i / 100)
            sleep(0.01)
            self.root.update()

    def create_widgets(self):
        # Use a frame to hold all content (helps with style)
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Length input
        ttk.Label(main_frame, text="Enter Password Length (min 4)").pack(pady=5)
        length_entry = ttk.Entry(main_frame, textvariable=self.password_length, width=5)
        length_entry.pack()

        # Checkboxes
        ttk.Checkbutton(
            main_frame, text="Include Letters", variable=self.use_letters
        ).pack(pady=5)
        ttk.Checkbutton(
            main_frame, text="Include Numbers", variable=self.use_numbers
        ).pack(pady=5)
        ttk.Checkbutton(
            main_frame, text="Include Symbols", variable=self.use_symbols
        ).pack(pady=5)

        # Progress bar (initially hidden/empty)
        self.progress_bar = ttk.Progressbar(
            main_frame, orient="horizontal", length=200, mode="determinate"
        )
        self.progress_bar.pack(pady=10)
        self.progress_bar.pack_forget()  # Hide until generating

        # Generate button
        ttk.Button(
            main_frame, text="Generate Password", command=self.generate_password
        ).pack(pady=10)

        # Result display
        self.result_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.result_var, width=50).pack(pady=10)

        # Copy button
        ttk.Button(
            main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard
        ).pack(pady=10)

    def generate_password(self):
        # Show the progress bar and animate
        self.progress_bar.pack(pady=10)
        self.progress_bar["value"] = 0
        self.progress_bar.update()

        # Animate the progress bar (just a small fancy effect)
        for i in range(101):
            self.progress_bar["value"] = i
            self.root.update_idletasks()
            sleep(0.005)  # Adjust speed as desired

        # Now generate the actual password
        try:
            length = self.password_length.get()
            if length <= 0:
                self.result_var.set("Length must be positive")
                return
            elif length < 4:
                self.result_var.set("Password must be at least 4 characters long")
                return

            chars = ""
            if self.use_letters.get():
                chars += ascii_letters
            if self.use_numbers.get():
                chars += digits
            if self.use_symbols.get():
                chars += punctuation

            if not chars:
                self.result_var.set("Select at least one character type")
                return

            password = [choice(chars) for _ in range(length)]
            self.result_var.set("".join(password))

        except ValueError:
            self.result_var.set("Please enter a valid number")

    def copy_to_clipboard(self):
        password = self.result_var.get()
        if password and password not in [
            "Length must be positive",
            "Select at least one character type",
            "Please enter a valid number",
            "Password must be at least 4 characters long",
        ]:
            copy(password)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
