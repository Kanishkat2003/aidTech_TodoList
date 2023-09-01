import pickle

# Define a class Task
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "Incomplete"

    def mark_as_completed(self):
        self.status = "Completed"

# Define a class ToDoList
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. Title: {task.title}, Description: {task.description}, Status: {task.status}")

    def save_tasks(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            print("File not found. No tasks loaded.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == '2':
            index = int(input("Enter the index of the task to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            filename = input("Enter filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == '5':
            filename = input("Enter filename to load tasks from: ")
            todo_list.load_tasks(filename)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
