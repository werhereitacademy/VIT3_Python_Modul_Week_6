# VIT3_Python_Modul_Week_6
![resim](https://github.com/werhereitacademy/week_6/assets/141542413/1b3ec14b-5895-4afc-8cb1-df7c34139323)
#### Overview
This Python program is a simple Task Management System that allows users to create, edit, track, and display tasks. It uses Object-Oriented Programming (OOP) principles to create a structured system for managing tasks.
##### Prerequisites
Before working on this program, students should have a basic understanding of the following concepts:
1. Python programming fundamentals (variables, functions, classes, objects).
2. Inheritance and abstract classes in Python.
3. Working with dates and times in Python (using the datetime module).
4. Exception handling in Python.
5. Basic knowledge of interfaces/abstract classes (Python ABC).
### Program Structure
1.Task Management Class (TaskManagement):
* This class serves as the core of the task management system.
* It contains a list (taskList) to store tasks.
* It provides methods to add and display tasks.
  
2.Task Scheduling Class (TaskScheduling):
* This class is responsible for creating and adding tasks to the TaskManagement instance.
* It uses the PersonalTask and WorkTask classes to create specific types of tasks.
* It enforces proper task type (Personal or Work).
  
3.Task Editing Class (TaskEditing):
* This class handles various editing operations on tasks.
* Students will learn how to modify task attributes such as status, priority, and deadline.
* They will also learn about searching for tasks and removing tasks from the list.
  
4.Task Tracking Class (TaskTracking):
* This class allows tracking task statuses.
* Students will learn how to retrieve the status of a task and mark tasks as completed.
  
5.Abstract Base Class (Task):
* An abstract base class defines the common structure for PersonalTask and WorkTask subclasses.
* It introduces the concept of abstract methods and demonstrates inheritance.
  
6.PersonalTask and WorkTask Classes:
* These are subclasses of the ‘Task’ class, representing personal and work-related tasks.
* Students will understand how to override methods and use class-specific attributes.
* They will see how to implement interfaces/abstract classes (‘Priorization’).
  
7.Special Keywords Dictionary (SPECIAL_KEYWORDS):
* A dictionary is used to handle special keywords like "today," "tomorrow," and "next week" for deadlines.
* Students will learn about dictionary usage and date manipulation.
  
#### Key Learning Points
* Object-Oriented Programming concepts (classes, objects, inheritance, abstract classes).
* Proper encapsulation and data hiding.
* Exception handling for task lookup.
* Working with dates and times using the datetime module.
* Using dictionaries for mapping special keywords.
* Implementing interfaces/abstract classes in Python.
  
#### Assignment/Exercises for Students
1. Create a new task type (e.g., "StudyTask") by extending the program. Implement its specific behavior and attributes.
2. Add more editing operations (e.g., change task color or add notes).
3. Implement a feature to sort tasks by priority or deadline.
4. Create a user interface (e.g., a command-line or graphical interface) to interact with the task management system.
5. Write unit tests to ensure the program's functionality is correct.
   
- By working on these exercises, students can deepen their understanding of OOP principles and improve their Python programming skills.

##### Exp: Let's consider an example where we create, edit, and track tasks using your program:
![resim](https://github.com/werhereitacademy/week_6/assets/141542413/bf32d5d1-9b8a-421c-a165-713a32c5460b)

##### Expected Output:
![resim](https://github.com/werhereitacademy/week_6/assets/141542413/cc842474-4df4-4820-9668-89193eddfec3)


## Hackerrank Questions

1. sWAP cASE: https://www.hackerrank.com/challenges/swap-case/problem

2. String Split and Join: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

3. Mutations: https://www.hackerrank.com/challenges/python-mutations/problem

4. Text Wrap: https://www.hackerrank.com/challenges/text-wrap/problem
