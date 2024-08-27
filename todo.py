import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.config(bg="#2c3e50")
        title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 24, "bold"), bg="#2c3e50", fg="#ecf0f1")
        title_label.pack(pady=20)
        self.task_listbox = tk.Listbox(root, height=15, width=40, bg="#34495e", fg="#ecf0f1", font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)
        self.entry_task = tk.Entry(root, width=30, font=("Helvetica", 12), bg="#ecf0f1", fg="#2c3e50")
        self.entry_task.pack(pady=10)
        button_frame = tk.Frame(root, bg="#2c3e50")
        button_frame.pack(pady=20)
        add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, width=10, bg="#27ae60", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
        add_button.grid(row=0, column=0, padx=10)
        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, width=10, bg="#c0392b", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
        delete_button.grid(row=0, column=1, padx=10)
        edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task, width=10, bg="#f39c12", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
        edit_button.grid(row=1, column=0, padx=10, pady=5)
        clear_button = tk.Button(button_frame, text="Clear All", command=self.clear_all_tasks, width=10, bg="#e74c3c", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
        clear_button.grid(row=1, column=1, padx=10, pady=5)
        self.tasks = []

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = simpledialog.askstring("Edit Task", "Edit the selected task:", initialvalue=self.tasks[selected_task_index[0]])
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def clear_all_tasks(self):
        self.tasks.clear()
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
