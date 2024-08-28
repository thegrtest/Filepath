import tkinter as tk
from tkinter import filedialog

def select_file():
    # Initialize Tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file explorer and ask the user to select a file
    file_path = filedialog.askopenfilename(title="Select a File")

    # Check if a file was selected
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected.")

if __name__ == "__main__":
    select_file()
