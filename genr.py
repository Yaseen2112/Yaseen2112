import tkinter as tk
import string
import random

def generate_password():
    length = int(length_entry.get())
    characters = ''
    if var_lowercase.get():
        characters += string.ascii_lowercase
    if var_uppercase.get():
        characters += string.ascii_uppercase
    if var_digits.get():
        characters += string.digits
    if var_special.get():
        characters += string.punctuation
    if not characters:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")

# Set window size
window_width = 604
window_height = 378

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set window position and size
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Background color
root.config(bg="#f0f0f0")

# Frame for centered content
frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.SOLID)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Heading
heading = tk.Label(root, text="Password Generator", font=("Arial", 24, "bold"), bg="#f0f0f0")
heading.place(relx=0.5, y=10, anchor='n')

tk.Label(frame, text="Password Length:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky='e')
length_entry = tk.Entry(frame, width=10, font=("Arial", 12), bd=2, relief=tk.SOLID)
length_entry.grid(row=0, column=1, padx=5, pady=5)

var_lowercase = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Lowercase", variable=var_lowercase, font=("Arial", 12), bg="#f0f0f0", bd=1, relief=tk.RAISED).grid(row=1, column=0, columnspan=2, sticky='w', padx=5, pady=5)

var_uppercase = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Uppercase", variable=var_uppercase, font=("Arial", 12), bg="#f0f0f0", bd=1, relief=tk.RAISED).grid(row=2, column=0, columnspan=2, sticky='w', padx=5, pady=5)

var_digits = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Digits", variable=var_digits, font=("Arial", 12), bg="#f0f0f0", bd=1, relief=tk.RAISED).grid(row=3, column=0, columnspan=2, sticky='w', padx=5, pady=5)

var_special = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Special Characters", variable=var_special, font=("Arial", 12), bg="#f0f0f0", bd=1, relief=tk.RAISED).grid(row=4, column=0, columnspan=2, sticky='w', padx=5, pady=5)

tk.Button(frame, text="Generate Password", command=generate_password, font=("Arial", 14), bg="#4CAF50", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

tk.Label(frame, text="Generated Password:", font=("Arial", 12), bg="#f0f0f0").grid(row=6, column=0, padx=5, pady=5, sticky='e')
password_entry = tk.Entry(frame, width=30, font=("Arial", 12), bd=2, relief=tk.SOLID)
password_entry.grid(row=6, column=1, padx=5, pady=5)

root.mainloop()
