import tkinter as tk
root = tk.Tk()
root.title("Simple Calculator")
entry = tk.Entry(root, width=16, borderwidth=3, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_operator(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + operator)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('+', 4, 1), ('=', 4, 2), ('C', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=button_equal).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=button_clear).grid(row=row, column=col)
    elif text in '+-*/':
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: button_operator(t)).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: button_click(t)).grid(row=row, column=col)

root.mainloop()
