from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Task(ABC):
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "Incomplete"

    def __str__(self):
        return f"Description: {self.description}, Deadline: {self.deadline}, Status: {self.status}"

    @abstractmethod
    def prioritize(self):
        pass

class PersonalTask(Task):
    def prioritize(self):
        return "Low"

class WorkTask(Task):
    def prioritize(self):
        return "High"

class TaskManagement:
    def __init__(self):
        self.taskList = []

    def add_task(self, task):
        self.taskList.append(task)

    def display_tasks(self):
        for task in self.taskList:
            print(task)

class TaskScheduling:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def create_task(self):
        description = input("Enter task description: ")
        deadline = input("Enter task deadline (YYYY-MM-DD): ")
        task_type = input("Enter task type (Personal/Work): ")
        if task_type == "Personal":
            task = PersonalTask(description, deadline)
        elif task_type == "Work":
            task = WorkTask(description, deadline)
        else:
            raise ValueError("Invalid task type")
        self.task_manager.add_task(task)

class TaskEditing:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def edit_task_status(self):
        task = input("Enter task description to edit status: ")
        new_status = input("Enter new status for the task: ")
        for t in self.task_manager.taskList:
            if t.description == task:
                t.status = new_status
                return
        print("Task not found")

    def search_task(self):
        keyword = input("Enter keyword to search for task: ")
        for task in self.task_manager.taskList:
            if keyword in task.description:
                print(task)

    def remove_task(self):
        task = input("Enter task description to remove: ")
        for t in self.task_manager.taskList:
            if t.description == task:
                self.task_manager.taskList.remove(t)
                return
        print("Task not found")

class TaskTracking:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def get_task_status(self):
        task = input("Enter task description to get status: ")
        for t in self.task_manager.taskList:
            if t.description == task:
                print(f"Status of task '{task}': {t.status}")
                return
        print("Task not found")

    def mark_task_completed(self):
        task = input("Enter task description to mark as completed: ")
        for t in self.task_manager.taskList:
            if t.description == task:
                t.status = "Completed"
                print(f"Task '{task}' marked as completed.")
                return
        print("Task not found")

class SpecialKeywords:
    def __init__(self):
        self.keywords = {
            "today": datetime.now().strftime("%Y-%m-%d"),
            "tomorrow": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
            "next week": (datetime.now() + timedelta(weeks=1)).strftime("%Y-%m-%d")
        }

    def get_date(self, keyword):
        return self.keywords.get(keyword.lower(), "Invalid keyword")

class TaskManagementSystem:
    def __init__(self):
        self.task_manager = TaskManagement()
        self.task_scheduler = TaskScheduling(self.task_manager)
        self.task_editor = TaskEditing(self.task_manager)
        self.task_tracker = TaskTracking(self.task_manager)
        self.special_keywords = SpecialKeywords()

    def run(self):
        while True:
            print("\nTask Management System Menu:")
            print("1. Add Task")
            print("2. Edit Task Status")
            print("3. Search Task")
            print("4. Remove Task")
            print("5. Get Task Status")
            print("6. Mark Task as Completed")
            print("7. Display Tasks")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.task_scheduler.create_task()
            elif choice == "2":
                self.task_editor.edit_task_status()
            elif choice == "3":
                self.task_editor.search_task()
            elif choice == "4":
                self.task_editor.remove_task()
            elif choice == "5":
                self.task_tracker.get_task_status()
            elif choice == "6":
                self.task_tracker.mark_task_completed()
            elif choice == "7":
                self.task_manager.display_tasks()
            elif choice == "8":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 8.")

# Example usage:
task_system = TaskManagementSystem()
task_system.run()
