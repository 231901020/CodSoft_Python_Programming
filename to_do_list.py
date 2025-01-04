import json

class ToDoListApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append({"title": title, "completed": False})
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available!")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "✔️" if task["completed"] else "❌"
                print(f"{idx}. {task['title']} - {status}")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Task '{self.tasks[index]['title']}' marked as completed!")
        else:
            print("Invalid task number!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else:
            print("Invalid task number!")

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file, indent=4)
        print("Tasks saved to file.")

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("No saved tasks found.")

    def run(self):
        self.load_tasks()
        while True:
            print("\n1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Save and Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                title = input("Enter task title: ").strip()
                if title:
                    self.add_task(title)
                else:
                    print("Task title cannot be empty!")
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.view_tasks()
                try:
                    index = int(input("Enter task number to mark as completed: ")) - 1
                    self.mark_completed(index)
                except ValueError:
                    print("Invalid input! Please enter a number.")
            elif choice == "4":
                self.view_tasks()
                try:
                    index = int(input("Enter task number to delete: ")) - 1
                    self.delete_task(index)
                except ValueError:
                    print("Invalid input! Please enter a number.")
            elif choice == "5":
                self.save_tasks()
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
