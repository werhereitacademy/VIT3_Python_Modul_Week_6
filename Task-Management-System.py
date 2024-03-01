from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class TaskManagement:
    def __init__(self):
        self.taskList = []

    def add(self, task):
        self.taskList.append(task)
        print("Task added successfully.")

    def display(self):
        if self.taskList:
            print("Your Tasks:")
            for task in self.taskList:
                print(task)
        else:
            print("No tasks found!")

class TaskScheduling:
    def __init__(self,task_management):
        self.task_management = task_management

    def create_task(self, task):
        title = task.title
        deadline_input = task.dead_line
        priority = task.priority
        color = task.color
        status = task.status
        while True:
            if deadline_input.lower() in SPECIAL_KEYWORDS:
                deadline = SPECIAL_KEYWORDS[deadline_input.lower()]
                break
            else:
                print("Invalid type")
                return

        task_type = input("Enter task type:\n"
                          "for 'Personel' press '1'\n"
                          "for 'Work' press '2'\n"
                          "to come back press 'q'")

        if task_type.lower() == "1":
            
            if priority in ["high", "low"]:
                bos_sira = self.bos_sira_bul_per()
                remaining_days = (deadline - datetime.now().date()).days
                new_task = {
                    "PersonalTask": bos_sira,
                    "Task": title,
                    "Priority": priority,
                    "Color": color,
                    "Remaining Day": remaining_days,
                    "Status":status
                }
                self.task_management.add(new_task)
            else:
                print("Invalid type")
                return
        elif task_type.lower() == "2":

            if priority in ["high", "low"]:
                bos_sira = self.bos_sira_bul_wor()
                remaining_days = (deadline - datetime.now().date()).days
                new_task = {
                    "WorkTask": bos_sira,
                    "Task": title,
                    "Priority": priority,
                    "Color": color,
                    "Remaining Day": remaining_days,
                    "Status":status
                }
                self.task_management.add(new_task)
            else:
                print("Invalid type")
                return
        elif task_type.lower() == "q":
            return
        else:
            print("Invalid task type.")

    def bos_sira_bul_per(self):
        sira_numaralari = []
        for islem in self.task_management.taskList:
            if "PersonalTask" in islem:
                sira_numaralari.append(islem["PersonalTask"])

        sira_numaralari.sort()

        for i, sira in enumerate(sira_numaralari, start=1):
            if i != sira:
                return i

        return len(sira_numaralari) + 1

    def bos_sira_bul_wor(self):
        sira_numaralari = []
        for islem in self.task_management.taskList:
            if "WorkTask" in islem:
                sira_numaralari.append(islem["WorkTask"])

        sira_numaralari.sort()

        for i, sira in enumerate(sira_numaralari, start=1):
            if i != sira:
                return i

        return len(sira_numaralari) + 1


class TaskEditing:
    def __init__(self, task_management):
        self.task_management = task_management

    def edit_task(self):
        title_edit_input = input("Enter the title of the task you want to edit: ")

        for task in self.task_management.taskList:
            if task["Task"] == title_edit_input:
                selection = input("What do you want to change?\n"
                                  "for status press '1'\n"
                                  "for priority press '2'\n"
                                  "for deadline press '3'\n"
                                  "to come back press 'q'\n")

                if selection == "1":
                    new_status = input("Enter new status (completed/not completed): ").lower()
                    if new_status in ["completed", "not completed"]:
                        print("Status:"," was", task["Status"])
                        task["Status"] = new_status
                        print("The update has been performed.")
                        print(task)
                        return
                    else:
                        print("Invalid input!")
                elif selection == "2":
                    new_priority = input("Enter new priority (low/high): ").lower()
                    if new_priority in ["low", "high"]:
                        print("Current Priority:", task["Priority"])
                        task["Priority"] = new_priority
                        print("The update has been performed.")
                        print(task)
                    else:
                        print("Invalid input!")

                elif selection == "3":
                    new_deadline_input = input("Enter new deadline (use: 'today', 'tomorrow' or 'next week'): ").lower()
                    if new_deadline_input in SPECIAL_KEYWORDS:
                        new_deadline = SPECIAL_KEYWORDS[new_deadline_input]
                        remaining_days = (new_deadline - datetime.now().date()).days
                        print("Current Deadline:", task["Remaining Day"], "days remaining")
                        task["Remaining Day"] = remaining_days
                        print("The update has been performed.")
                        print(task)
                        return
                    else:
                        print("Invalid input!")
                elif selection == "q":
                    return
                else:
                    print("Invalid input!")
        else:
            print("Task not found.")

    def searching_task(self):
        title_edit_input = input("Enter the title of the task you want to search: ")

        for task in self.task_management.taskList:
            if task["Task"] == title_edit_input:
                print(task)
                return

        else:
            print("Invalid input!")

    def removing_task(self):
        title_edit_input = input("Enter the title of the task you want to search: ")

        for task in self.task_management.taskList:
            if task["Task"] == title_edit_input:
                self.task_management.taskList.remove(task)
                print("Removing completed successfully.")
                return

        else:
            print("Invalid input!")


class TaskTracking:
    def __init__(self,task_management):
        self.task_management = task_management

    def show_task_status(self):
        task_input = input("Enter the title of the task you want to search: ")

        for task in self.task_management.taskList:
            if task["Task"] == task_input:
                print("Current status of your task:")
                print(task["Status"])
                return
        else:
            print("Invalid input!")

    def retrieve(self):
        task_input = input("Enter the title of the task you want to search: ")

        for task in self.task_management.taskList:
            if task["Status"] == "not completed":
                print("The situation is already'not completed'")

            elif task["Status"] == "completed":
                task["Status"] = "not completed"
                print("Updated with success.")

        else:
            print("Invalid input!")

class Task(ABC):
    def __init__(self, title, deadline_input, priority,color, status="not completed", ):
        self.title = title
        self.dead_line = deadline_input
        self.priority = priority
        self.status = status
        self.color = color

    @abstractmethod
    def display_info(self):
        pass
class PersonalTask(Task):
    def __init__(self, title, deadline_input, priority,color, status="not completed",):
        super().__init__(title, deadline_input, priority,color, status)
    def display_info(self):
        print(f"Personal Task: {self.title}, Deadline: {self.dead_line}, Priority: {self.priority}")

class WorkTask(Task):
    def __init__(self, title, deadline_input, priority,color, status="not completed", ):
        super().__init__(title, deadline_input, priority,color, status)
    def display_info(self):
        print(f"Work Task: {self.title}, Deadline: {self.dead_line}, Priority: {self.priority}")

SPECIAL_KEYWORDS = {
    "today": datetime.now().date(),
    "tomorrow": datetime.now().date() + timedelta(days=1),
    "next week": datetime.now().date() + timedelta(weeks=1)
}

if __name__ == "__main__":
    task_management = TaskManagement()
    task_scheduling = TaskScheduling(task_management)
    task_editing = TaskEditing(task_management)
    task_tracking = TaskTracking(task_management)

    while True:
        print("\n1. Create Task\n2. Display Tasks\n3. Edit Task\n4. Remove Task\n5. Searching Task\n6. Retrieve Task Status\n7. Searching Task Status\n8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            dead_line_input = input("Enter deadline(use: `today` , `tomorrow` or `next week`")
            priority = input("Enter priority:low/high ")
            color = input("Enter color name ")
            personel=PersonalTask(title,dead_line_input,priority,color)
            task_scheduling.create_task(personel)

        elif choice == "2":
            task_management.display()
        elif choice == "3":
            task_editing.edit_task()
        elif choice == "4":
            task_editing.removing_task()
        elif choice == "5":
            task_editing.searching_task()
        elif choice == "6":
            task_tracking.retrieve()
        elif choice == "7":
            task_tracking.show_task_status()
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
