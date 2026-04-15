import heapq
import tkinter as tk
from tkinter import messagebox
class Task:
    def __init__(self, name, priority, duration, dependency=None):
        self.name = name
        self.priority = priority
        self.duration = duration
        self.dependency = dependency
    def __lt__(self, other):
        return self.priority < other.priority
class Scheduler:
    def __init__(self):
        self.queue = []
        self.completed = set()
    def add_task(self, task):
        heapq.heappush(self.queue, task)
    def run(self):
        output = ""
        current_time = 0
        attempts = 0
        max_attempts = len(self.queue) * 2
        while self.queue and attempts < max_attempts:
            task = heapq.heappop(self.queue)
            if task.dependency and task.dependency not in self.completed:
                heapq.heappush(self.queue, task)
                attempts += 1
                continue
            output += f"Executing {task.name} at time {current_time}\n"
            current_time += task.duration
            self.completed.add(task.name)
            attempts = 0
        if self.queue:
            output += "\n⚠️ Deadlock detected!"
        return output
scheduler = Scheduler()
def add_task():
    name = name_entry.get()
    priority = priority_entry.get()
    duration = duration_entry.get()
    dependency = dep_entry.get()
    if not name or not priority or not duration:
        messagebox.showerror("Error", "Fill all required fields")
        return
    try:
        task = Task(
            name,
            int(priority),
            int(duration),
            dependency if dependency else None
        )
    except ValueError:
        messagebox.showerror("Error", "Priority and Duration must be numbers")
        return
    scheduler.add_task(task)
    messagebox.showinfo("Success", f"Task '{name}' added")
def run_tasks():
    result = scheduler.run()
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)
root = tk.Tk()
root.title("Task Scheduler")
tk.Label(root, text="Task Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Priority").pack()
priority_entry = tk.Entry(root)
priority_entry.pack()
tk.Label(root, text="Duration").pack()
duration_entry = tk.Entry(root)
duration_entry.pack()
tk.Label(root, text="Dependency (optional)").pack()
dep_entry = tk.Entry(root)
dep_entry.pack()
tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Run Scheduler", command=run_tasks).pack()
output_box = tk.Text(root, height=10, width=40)
output_box.pack()
root.mainloop()