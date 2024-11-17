
# Simple To-Do List Application

class ToDoList:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        """Load tasks from a file."""
        try:
            with open('todo_list.txt', 'r') as file:
                for line in file:
                    task, completed = line.strip().split('||')
                    self.tasks.append({"task": task, "completed": completed == 'True'})
        except FileNotFoundError:
            pass  # If the file doesn't exist, start with an empty list.

    def save_tasks(self):
        """Save tasks to a file."""
        with open('todo_list.txt', 'w') as file:
            for task in self.tasks:
                f"{task['task']}||{task['completed']}\n"1
                

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        """Return a list of all tasks with their status."""
        return [
            f"{idx + 1}. {'[X]' if task['completed'] else '[ ]'} {task['task']}"
            for idx, task in enumerate(self.tasks)
        ]

    def complete_task(self, task_number):
        """Mark a task as completed."""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True

    def delete_task(self, task_number):
        """Delete a task from the list."""
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.load_tasks()

    while True:
        print("\nTo-Do List:")
        for task in todo_list.view_tasks():
            print(task)

        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            todo_list.save_tasks()
        elif choice == "2":
            task_num = int(input("Enter task number to complete: "))
            todo_list.complete_task(task_num)
            todo_list.save_tasks()
        elif choice == "3":
            task_num = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_num)
            todo_list.save_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")
