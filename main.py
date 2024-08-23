import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority, category):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.category = category

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Task Manager")
        
        self.tasks = []
        
        self.setup_gui()
    
    def setup_gui(self):
        
        self.task_listbox = tk.Listbox(self.root, width=50, height=15)
        self.task_listbox.grid(row=0, column=0, rowspan=6, padx=10, pady=10)
        
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.grid(row=0, column=1, rowspan=6, sticky="ns")
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
       
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=5)
        
        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=1, column=2, padx=10, pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=2, padx=10, pady=5)
        
        self.sort_priority_button = tk.Button(self.root, text="Sort by Priority", command=self.sort_by_priority)
        self.sort_priority_button.grid(row=3, column=2, padx=10, pady=5)
        
        self.sort_date_button = tk.Button(self.root, text="Sort by Due Date", command=self.sort_by_due_date)
        self.sort_date_button.grid(row=4, column=2, padx=10, pady=5)
        
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.grid(row=5, column=2, padx=10, pady=5)

    def add_task(self):
        name = simpledialog.askstring("Task Name", "Enter the task name:")
        if not name:
            return
        
        due_date_str = simpledialog.askstring("Due Date", "Enter the due date (YYYY-MM-DD):")
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
            return
        
        priority = simpledialog.askinteger("Priority", "Enter priority (1-5):", minvalue=1, maxvalue=5)
        if priority is None:
            return
        
        category = simpledialog.askstring("Category", "Enter the task category:")
        if not category:
            return
        
        task = Task(name, due_date, priority, category)
        self.tasks.append(task)
        self.update_task_listbox()
    
    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Select Task", "Please select a task to edit.")
            return
        
        task = self.tasks[selected_index[0]]
        
        new_name = simpledialog.askstring("Edit Task", "Enter new task name:", initialvalue=task.name)
        if not new_name:
            return
        
        new_due_date_str = simpledialog.askstring("Edit Due Date", "Enter new due date (YYYY-MM-DD):", initialvalue=task.due_date.strftime("%Y-%m-%d"))
        try:
            new_due_date = datetime.strptime(new_due_date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
            return
        
        new_priority = simpledialog.askinteger("Edit Priority", "Enter new priority (1-5):", initialvalue=task.priority, minvalue=1, maxvalue=5)
        if new_priority is None:
            return
        
        new_category = simpledialog.askstring("Edit Category", "Enter new task category:", initialvalue=task.category)
        if not new_category:
            return
        
        task.name = new_name
        task.due_date = new_due_date
        task.priority = new_priority
        task.category = new_category
        
        self.update_task_listbox()
    
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Select Task", "Please select a task to delete.")
            return
        
        del self.tasks[selected_index[0]]
        self.update_task_listbox()
    
    def sort_by_priority(self):
        self.tasks.sort(key=lambda task: task.priority)
        self.update_task_listbox()
    
    def sort_by_due_date(self):
        self.tasks.sort(key=lambda task: task.due_date)
        self.update_task_listbox()
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_str = f"{task.name} | Due: {task.due_date.strftime('%Y-%m-%d')} | Priority: {task.priority} | Category: {task.category}"
            self.task_listbox.insert(tk.END, task_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
