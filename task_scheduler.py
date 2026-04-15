import heapq
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
        self.tasks = {}
    def add_task(self, task):
        self.tasks[task.name] = task
        heapq.heappush(self.queue, task)
        print(f"Task '{task.name}' added.")
    def run(self):
        print("\nRunning Tasks:\n")
        attempts = 0
        max_attempts = len(self.queue) * 2
        while self.queue and attempts < max_attempts:
            task = heapq.heappop(self.queue)
            if task.dependency and task.dependency not in self.completed:
                print(f"Skipping {task.name}, waiting for {task.dependency}")
                heapq.heappush(self.queue, task)
                attempts += 1
                continue
            print(f"Executing {task.name}")
            self.completed.add(task.name)
            attempts = 0
        if self.queue:
            print("\n⚠️ Deadlock detected or invalid dependencies!")
scheduler = Scheduler()
while True:
    print("\n1. Add Task")
    print("2. Run Tasks")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Task Name: ")
        priority = int(input("Priority: "))
        duration = int(input("Duration: "))
        dep = input("Dependency (leave blank if none): ")
        dep = dep if dep != "" else None
        task = Task(name, priority, duration, dep)
        scheduler.add_task(task)
    elif choice == "2":
        scheduler.run()
    elif choice == "3":
        break
    else:
        print("Invalid choice")