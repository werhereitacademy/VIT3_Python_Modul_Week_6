import datetime
from abc import ABC, abstractmethod


class Task(ABC):
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.status = False

    @abstractmethod
    def display_details(self):
        pass


class PersonalTask(Task):
    priority = 'Low'
    color = 'Yellow'

    def display_details(self):
        status = "Completed" if self.status else "Pending"
        print(f"Personal Task: {self.name}\n"
              f"Priority     : {self.priority}\n"
              f"Deadline     : {self.deadline}\n"
              f"Color        : {self.color}\n"
              f"Status       : {status}")


class WorkTask(Task):
    priority = 'High'
    color = 'Red'

    def display_details(self):
        status = "Completed" if self.status else "Pending"
        print(f"Personal Task: {self.name}\n"
              f"Priority     : {self.priority}\n"
              f"Deadline     : {self.deadline}\n"
              f"Color        : {self.color}\n"
              f"Status       : {status}")


class StudyTask(Task):
    priority = 'Medium'
    color = 'Green'

    def display_details(self):
        status = "Completed" if self.status else "Pending"
        print(f"Personal Task: {self.name}\n"
              f"Priority     : {self.priority}\n"
              f"Deadline     : {self.deadline}\n"
              f"Color        : {self.color}\n"
              f"Status       : {status}")


SPECIAL_KEYWORDS = {'today': datetime.datetime.today().strftime("%x %X"),
                    'tomorrow': (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%x"),
                    'next_week': (datetime.datetime.today() + datetime.timedelta(days=7)).strftime("%x")
                    }


class TaskManagement:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def display_tasks(self):
        if not self.task_list:
            print("No tasks to display.")
            return
        print("Tasks:")
        for i in self.task_list:
            i.display_details()


class TaskScheduling:
    @staticmethod
    def add_personal_task(name, deadline):
        return PersonalTask(name, deadline)

    @staticmethod
    def add_work_task(name, deadline):
        return WorkTask(name, deadline)

    @staticmethod
    def add_study_task(name, deadline):
        return StudyTask(name, deadline)


class TaskEditing:

    @staticmethod
    def mark_completed(task):
        task.status = True

    @staticmethod
    def change_deadline(task, new_deadline):
        task.deadline = new_deadline

    @staticmethod
    def change_priority(task, prio):
        task.priority = prio

    @staticmethod
    def change_color(task, new_color):
        task.color = new_color

    @staticmethod
    def remove_task(tm_instance, task):
        return tm_instance.task_list.remove(task)


class TaskTracking:
    @staticmethod
    def get_tasks(task_management):
        task_management.display_tasks()

    @staticmethod
    def search_task(tm_instance, task_name):
        result = False
        for i in tm_instance.task_list:
            if task_name.lower() in i.name.lower():
                result = i
                break
        return result


if __name__ == '__main__':
    wtask1 = TaskScheduling.add_work_task('Ise git', SPECIAL_KEYWORDS['today'])
    ptask1 = TaskScheduling.add_personal_task('Uyu len', SPECIAL_KEYWORDS['tomorrow'])
    stask1 = TaskScheduling.add_study_task('Odevi yap!', SPECIAL_KEYWORDS['next_week'])
    ptask2 = TaskScheduling.add_personal_task('Uyan', SPECIAL_KEYWORDS['today'])

    tm = TaskManagement()
    tm.add_task(wtask1)
    tm.add_task(ptask1)
    tm.add_task(stask1)
    tm.add_task(ptask2)
    tm.display_tasks()
    print('-' * 40)

    te = TaskEditing()
    te.mark_completed(ptask1)
    tm.display_tasks()
    print('-' * 40)

    te.remove_task(tm, ptask2)
    tm.display_tasks()
    print('-' * 40)

    te.change_deadline(ptask1, SPECIAL_KEYWORDS['next_week'])
    tm.display_tasks()
    print('-' * 40)

    print('You will see the list two times!!!')
    tt = TaskTracking()
    tt.get_tasks(tm)
    tm.display_tasks()
    print('-' * 40)

    searched_task = TaskTracking.search_task(tm, 'ode')
    searched_task.display_details()
