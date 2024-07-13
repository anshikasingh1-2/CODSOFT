import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.tasks = []

        self.heading = tk.Label(self.root, text="To-Do List", font=("Helvetica", 20, "bold"), fg="blue")
        self.heading.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(
            self.frame, width=50, height=10, selectmode=tk.SINGLE, bg="#f0f0f0", fg="#000000", font=("Helvetica", 12))
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_text = tk.StringVar()
        self.entry_task = tk.Entry(self.root, width=50, font=("Helvetica", 12), textvariable=self.entry_text, fg="grey")
        self.entry_task.insert(0, "Add a task")
        self.entry_task.bind("<FocusIn>", self.clear_entry)
        self.entry_task.bind("<FocusOut>", self.restore_entry)
        self.entry_task.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        button_style = {"font": ("Helvetica", 12), "width": 20, "height": 2, "bg": "lightblue", "fg": "black"}

        self.button_add_task = tk.Button(button_frame, text="Add Task", command=self.add_task, **button_style)
        self.button_add_task.pack(pady=5)

        self.button_edit_task = tk.Button(button_frame, text="Edit Task", command=self.edit_task, **button_style)
        self.button_edit_task.pack(pady=5)

        self.button_delete_task = tk.Button(button_frame, text="Delete Task", command=self.delete_task, **button_style)
        self.button_delete_task.pack(pady=5)

        self.button_mark_complete = tk.Button(button_frame, text="Mark as Complete", command=self.mark_complete, **button_style)
        self.button_mark_complete.pack(pady=5)

    def clear_entry(self, event):
        if self.entry_task.get() == "Add a task":
            self.entry_task.delete(0, tk.END)
            self.entry_task.config(fg="black")

    def restore_entry(self, event):
        if self.entry_task.get() == "":
            self.entry_task.insert(0, "Add a task")
            self.entry_task.config(fg="grey")

    def add_task(self):
        task = self.entry_task.get()
        if task and task != "Add a task":
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry_task.delete(0, tk.END)
            self.restore_entry(None)  
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def edit_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.tasks[selected_task_index]
            new_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=selected_task)
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def mark_complete(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = task + " (Completed)"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
