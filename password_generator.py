import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        
        # Define the character sets
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        password_var.set(password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Enter password length:").grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=1, column=0, columnspan=2, pady=10)

tk.Label(root, text="Generated Password:").grid(row=2, column=0, padx=10, pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, width=40, state='readonly')
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
